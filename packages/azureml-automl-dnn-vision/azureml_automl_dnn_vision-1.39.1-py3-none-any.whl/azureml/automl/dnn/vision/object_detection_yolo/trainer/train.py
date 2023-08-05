# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

""" Contain functions for training and validation """

import copy
import gc
import math
import numpy as np
import os
import random
import time
import torch
from typing import Any, Dict

from azureml.automl.core.shared.constants import Tasks
from azureml.automl.dnn.vision.common import utils
from azureml.automl.dnn.vision.common.artifacts_utils import save_model_checkpoint, write_artifacts
from azureml.automl.dnn.vision.common.average_meter import AverageMeter
from azureml.automl.dnn.vision.common.constants import TrainingCommonSettings, \
    SettingsLiterals as CommonSettingsLiterals, TrainingLiterals as CommonTrainingLiterals
from azureml.automl.dnn.vision.common.logging_utils import get_logger
from azureml.automl.dnn.vision.common.system_meter import SystemMeter
from azureml.automl.dnn.vision.common.trainer.lrschedule import LRSchedulerUpdateType
from azureml.automl.dnn.vision.object_detection.common import boundingbox
from azureml.automl.dnn.vision.object_detection.common.constants import ValidationMetricType, TrainingLiterals,\
    TilingLiterals
from azureml.automl.dnn.vision.object_detection.common.object_detection_utils import compute_metrics, \
    write_per_label_metrics_file
from azureml.automl.dnn.vision.object_detection.common.tiling_helper import merge_predictions_from_tiles_and_images
from azureml.automl.dnn.vision.object_detection.data.dataset_wrappers import DatasetProcessingType
from azureml.automl.dnn.vision.object_detection.eval import cocotools, vocmap
from azureml.automl.dnn.vision.object_detection.eval.incremental_voc_evaluator import IncrementalVocEvaluator
from azureml.automl.dnn.vision.object_detection.eval.utils import prepare_bounding_boxes_for_eval
from azureml.automl.dnn.vision.object_detection.writers.score_script_utils import write_scoring_script
from azureml.automl.dnn.vision.object_detection_yolo.common.constants import YoloLiterals
from azureml.automl.dnn.vision.object_detection_yolo.utils.ema import ModelEMA
from azureml.automl.dnn.vision.object_detection_yolo.utils.utils import compute_loss, non_max_suppression,\
    unpad_bbox, xywh2xyxy

logger = get_logger(__name__)


def train_one_epoch(model, ema, optimizer, scheduler, train_loader,
                    epoch, device, system_meter, grad_accum_steps, grad_clip_type: str,
                    print_freq=100, tb_writer=None):
    """Train a model for one epoch

    :param model: Model to train
    :type model: <class 'azureml.automl.dnn.vision.object_detection_yolo.models.yolo.Model'>
    :param ema: Model Exponential Moving Average
    :type ema: <class 'azureml.automl.dnn.vision.object_detection_yolo.utils.torch_utils.ModelEMA'>
    :param optimizer: Optimizer used in training
    :type optimizer: Pytorch optimizer
    :param scheduler: Learning Rate Scheduler wrapper
    :type scheduler: BaseLRSchedulerWrapper (see common.trainer.lrschedule)
    :param train_loader: Data loader for training data
    :type train_loader: Pytorch data loader
    :param epoch: Current training epoch
    :type epoch: int
    :param device: Target device
    :type device: Pytorch device
    :param system_meter: A SystemMeter to collect system properties
    :type system_meter: SystemMeter
    :param grad_accum_steps: gradient accumulation steps which is used to accumulate the gradients of those steps
     without updating model variables/weights
    :type grad_accum_steps: int
    :param clip_type: The type of gradient clipping. See GradClipType
    :type grad_clip_type: str
    :param print_freq: How often you want to print the output
    :type print_freq: int
    :param tb_writer: Tensorboard writer
    :type tb_writer: <class 'torch.utils.tensorboard.writer.SummaryWriter'>
    :returns: mean losses for tensorboard writer
    :rtype: <class 'torch.Tensor'>
    """

    batch_time = AverageMeter()
    data_time = AverageMeter()
    losses = AverageMeter()

    nb = len(train_loader)
    mloss = torch.zeros(4, device=device)  # mean losses (lbox, lobj, lcls, loss)

    model.train()

    # grad_accum_steps should be positive, smaller or equal than the number of batches per epoch
    grad_accum_steps = min(len(train_loader), max(grad_accum_steps, 1))
    logger.info("[grad_accumulation_step: {}]".format(grad_accum_steps))
    optimizer.zero_grad()

    end = time.time()
    for i, (imgs, targets, _) in enumerate(utils._data_exception_safe_iterator(iter(train_loader))):
        # measure data loading time
        data_time.update(time.time() - end)

        ni = i + nb * epoch  # number integrated batches (since train start)
        imgs = imgs.to(device).float() / 255.0  # uint8 to float32, 0 - 255 to 0.0 - 1.0

        # Multi scale : need more CUDA memory for bigger image size
        if model.hyp[YoloLiterals.MULTI_SCALE]:
            imgsz = model.hyp[YoloLiterals.IMG_SIZE]
            gs = model.hyp['gs']
            sz = random.randrange(imgsz * 0.5, imgsz * 1.5 + gs) // gs * gs
            sf = sz / max(imgs.shape[2:])
            if sf != 1:
                ns = [math.ceil(x * sf / gs) * gs for x in imgs.shape[2:]]  # new shape (stretched to gs-multiple)
                imgs = torch.nn.functional.interpolate(imgs, size=ns, mode='bilinear', align_corners=False)
            logger.info("{} is enabled".format(YoloLiterals.MULTI_SCALE))

        # Forward
        pred = model(imgs)

        # Loss
        loss, loss_items = compute_loss(pred, targets.to(device), model)
        loss /= grad_accum_steps
        loss_items /= grad_accum_steps
        # raise an UserException if loss is too big
        utils.check_loss_explosion(loss.item())
        loss.backward()

        if (i + 1) % grad_accum_steps == 0 or i == len(train_loader) - 1:
            # gradient clipping
            utils.clip_gradient(model.parameters(), grad_clip_type)
            optimizer.step()
            optimizer.zero_grad()
            ema.update(model)

        if scheduler.update_type == LRSchedulerUpdateType.BATCH:
            scheduler.lr_scheduler.step()

        # Tensorboard
        if tb_writer:
            tb_writer.add_scalar('lr', scheduler.lr_scheduler.get_last_lr()[0], ni)

        # record loss and measure elapsed time
        losses.update(loss.item(), len(imgs))
        mloss = (mloss * i + loss_items) / (i + 1)  # update mean losses
        batch_time.update(time.time() - end)
        end = time.time()

        # delete tensors which have a valid grad_fn
        del loss, pred

        if i % print_freq == 0 or i == nb - 1:
            mesg = "Epoch: [{0}][{1}/{2}]\t" "lr: {3:.5f}\t" "Time {batch_time.value:.4f} ({batch_time.avg:.4f})\t" \
                   "Data {data_time.value:.4f} ({data_time.avg:.4f})\t" "Loss {loss.value:.4f} " \
                   "({loss.avg:.4f})".format(epoch, i, nb, optimizer.param_groups[0]["lr"],
                                             batch_time=batch_time, data_time=data_time, loss=losses)
            logger.info(mesg)

            system_meter.log_system_stats()

    if scheduler.update_type == LRSchedulerUpdateType.EPOCH:
        scheduler.lr_scheduler.step()

    return mloss


def validate(
    model, val_index_map, validation_loader, incremental_evaluator, device, system_meter, conf_thres,
    nms_iou_threshold, tile_predictions_nms_thresh, tiling_merge_predictions_time, tiling_nms_time, print_freq=100
):
    """Gets model results on validation set.

    :param model: Model to score
    :type model: Pytorch nn.Module
    :param val_index_map: Map from numerical indices to class names
    :type val_index_map: List of strings
    :param validation_loader: Data loader for validation data
    :type validation_loader: Pytorch Data Loader
    :param incremental_evaluator: Incremental evaluator for object detection
    :type incremental_evaluator: IncrementalEvaluator
    :param device: Target device
    :type device: Pytorch device
    :param system_meter: A SystemMeter to collect system properties
    :type system_meter
    :param conf_thres: Confidence threshold
    :type conf_thres: float
    :param nms_iou_threshold: IOU threshold for NMS
    :type nms_iou_threshold: float
    :param tile_predictions_nms_thresh: The iou threshold to use to perform nms while merging predictions in tiling.
    :type tile_predictions_nms_thresh: float
    :param tiling_merge_predictions_time: Meter to record predictions merging time in tiling.
    :type tiling_merge_predictions_time: AverageMeter
    :param tiling_nms_time: Meter to record nms time when merging predictions in tiling.
    :type tiling_nms_time: AverageMeter
    :param print_freq: How often you want to print the output
    :type print_freq: int
    :return: Detections in format that can be consumed by cocotools/vocmap
    :rtype: List of dicts
    """

    batch_time = AverageMeter()

    nb = len(validation_loader)

    model.eval()

    bounding_boxes = []
    label_with_info_list = []

    end = time.time()
    for i, (imgs, targets, image_infos) in enumerate(utils._data_exception_safe_iterator(iter(validation_loader))):
        imgs = imgs.to(device).float() / 255.0

        with torch.no_grad():
            # inference and training outputs
            inf_out, _ = model(imgs)
            inf_out = inf_out.detach()

            # TODO: expose multi_label as arg to enable multi labels per box
            # Run NMS
            output = non_max_suppression(inf_out, conf_thres, nms_iou_threshold, multi_label=False)

        if incremental_evaluator is None:
            for image_info, image_output in zip(image_infos, output):
                label_with_info = {}
                label_with_info.update(image_info)

                height, width = unpad_bbox(image_output[:, :4] if image_output is not None else None,
                                           (image_info["height"], image_info["width"]), image_info["pad"])
                label_with_info["height"] = height
                label_with_info["width"] = width

                if image_output is not None:
                    boxes = image_output[:, :4]
                    labels = image_output[:, 5].to(dtype=torch.long)
                    scores = image_output[:, 4]

                    # move predictions to cpu to save gpu memory
                    label_with_info["boxes"] = boxes.cpu()
                    label_with_info["labels"] = labels.cpu()
                    label_with_info["scores"] = scores.cpu()
                else:
                    label_with_info["boxes"] = torch.empty(0, 4, dtype=torch.float, device="cpu")
                    label_with_info["labels"] = torch.empty(0, dtype=torch.long, device="cpu")
                    label_with_info["scores"] = torch.empty(0, dtype=torch.float, device="cpu")

                label_with_info_list.append(label_with_info)

        else:
            # Make detached versions of the output.
            output = [o.detach() if o is not None else None for o in output]

            # Convert labels and predictions to input format of incremental evaluator.
            gt_objects_per_image = _convert_all_targets_to_objects_per_image(targets, image_infos)
            predictions_per_image = _convert_predictions_to_objects_per_image(output, image_infos)

            # Do batch evaluation.
            incremental_evaluator.evaluate_batch(gt_objects_per_image, predictions_per_image, image_infos)

        # measure elapsed time
        batch_time.update(time.time() - end)
        end = time.time()

        if i % print_freq == 0 or i == nb - 1:
            mesg = "Test: [{0}/{1}]\t" \
                   "Time {batch_time.value:.4f} ({batch_time.avg:.4f})".format(i, nb,
                                                                               batch_time=batch_time)
            logger.info(mesg)

            system_meter.log_system_stats()

    if incremental_evaluator is None:
        if validation_loader.dataset.dataset_processing_type == DatasetProcessingType.IMAGES_AND_TILES:
            merged_label_with_info_list = merge_predictions_from_tiles_and_images(
                label_with_info_list=label_with_info_list, nms_thresh=tile_predictions_nms_thresh,
                device="cpu", merge_predictions_time=tiling_merge_predictions_time, nms_time=tiling_nms_time)
        else:
            merged_label_with_info_list = label_with_info_list

        for label_with_info in merged_label_with_info_list:
            image_boxes = boundingbox.ImageBoxes(label_with_info["filename"], val_index_map)
            image_boxes.add_boxes(label_with_info["boxes"],
                                  label_with_info["labels"],
                                  label_with_info["scores"])
            bounding_boxes.append(image_boxes)

        eval_bounding_boxes = prepare_bounding_boxes_for_eval(bounding_boxes)
        return eval_bounding_boxes

    return []


def train(model_wrapper, optimizer, scheduler, train_loader, validation_loader,
          output_dir=None, azureml_run=None, tb_writer=None):
    """Train a model

    :param model_wrapper: Model to train
    :type model_wrapper: BaseObjectDetectionModelWrapper
    :param optimizer: Optimizer used in training
    :type optimizer: Pytorch optimizer
    :param scheduler: Learning Rate Scheduler wrapper
    :type scheduler: BaseLRSchedulerWrapper (see common.trainer.lrschedule)
    :param train_loader: Data loader with training data
    :type train_loader: Pytorch data loader
    :param validation_loader: Data loader with validation data
    :type validation_loader: Pytorch data loader
    :param output_dir: Output directory to write checkpoints to
    :type output_dir: str
     :param azureml_run: azureml run object
    :type azureml_run: azureml.core.run.Run
    :param tb_writer: Tensorboard writer
    :type tb_writer: <class 'torch.utils.tensorboard.writer.SummaryWriter'>
    """

    epoch_time = AverageMeter()

    # Extract relevant parameters from training settings
    settings = model_wrapper.specs
    task_type = settings[CommonSettingsLiterals.TASK_TYPE]
    primary_metric = settings[CommonTrainingLiterals.PRIMARY_METRIC]
    val_index_map = model_wrapper.classes
    val_metric_type = settings[TrainingLiterals.VALIDATION_METRIC_TYPE]
    val_iou_threshold = settings[TrainingLiterals.VALIDATION_IOU_THRESHOLD]
    number_of_epochs = settings[CommonTrainingLiterals.NUMBER_OF_EPOCHS]
    enable_onnx_norm = settings[CommonSettingsLiterals.ENABLE_ONNX_NORMALIZATION]
    log_verbose_metrics = settings.get(CommonSettingsLiterals.LOG_VERBOSE_METRICS, False)
    is_enabled_early_stopping = settings[CommonTrainingLiterals.EARLY_STOPPING]
    early_stopping_patience = settings[CommonTrainingLiterals.EARLY_STOPPING_PATIENCE]
    early_stopping_delay = settings[CommonTrainingLiterals.EARLY_STOPPING_DELAY]
    eval_freq = settings[CommonTrainingLiterals.EVALUATION_FREQUENCY]
    checkpoint_freq = settings.get(CommonTrainingLiterals.CHECKPOINT_FREQUENCY, None)
    grad_accum_steps = settings[CommonTrainingLiterals.GRAD_ACCUMULATION_STEP]
    conf_thres = settings[YoloLiterals.BOX_SCORE_THRESH]
    nms_iou_threshold = settings[YoloLiterals.NMS_IOU_THRESH]
    grad_clip_type = settings[CommonTrainingLiterals.GRAD_CLIP_TYPE]
    save_as_mlflow = settings[CommonSettingsLiterals.SAVE_MLFLOW]
    tile_predictions_nms_thresh = settings[TilingLiterals.TILE_PREDICTIONS_NMS_THRESH]

    model = model_wrapper.model
    # Exponential moving average
    ema = ModelEMA(model)

    base_model = model
    device = model_wrapper.device

    best_model_wts = copy.deepcopy(ema.ema.state_dict())
    best_score = 0.0
    best_epoch = 0
    no_progress_counter = 0

    # Setup evaluation tools
    val_coco_index = None
    if val_metric_type in ValidationMetricType.ALL_COCO:
        val_coco_index = cocotools.create_coco_index(validation_loader.dataset)

    val_vocmap = None
    if val_metric_type in ValidationMetricType.ALL_VOC:
        # If no tiling, use incremental VOC evaluator.
        if validation_loader.dataset.dataset_processing_type != DatasetProcessingType.IMAGES_AND_TILES:
            val_metric_type = ValidationMetricType.INCREMENTAL_VOC
        else:
            val_vocmap = vocmap.VocMap(validation_loader.dataset, val_iou_threshold)

    computed_metrics: Dict[str, Any] = {}
    per_label_metrics: Dict[str, Any] = {}

    epoch_end = time.time()
    train_start = time.time()
    coco_metric_time = AverageMeter()
    voc_metric_time = AverageMeter()
    train_sys_meter = SystemMeter()
    valid_sys_meter = SystemMeter()
    tiling_merge_predictions_time = AverageMeter()
    tiling_nms_time = AverageMeter()

    specs = {
        'model_specs': model_wrapper.specs,
        'model_settings': model_wrapper.model_settings.get_settings_dict(),
        'classes': model_wrapper.classes,
        'inference_settings': model_wrapper.inference_settings
    }

    for epoch in range(number_of_epochs):

        mloss = train_one_epoch(base_model, ema, optimizer, scheduler, train_loader, epoch, device,
                                system_meter=train_sys_meter, grad_accum_steps=grad_accum_steps,
                                grad_clip_type=grad_clip_type, tb_writer=tb_writer)

        ema.update_attr(model)

        # Tensorboard
        if tb_writer:
            tags = ['train/giou_loss', 'train/obj_loss', 'train/cls_loss']
            for x, tag in zip(list(mloss[:-1]), tags):
                tb_writer.add_scalar(tag, x, epoch)

        # save model checkpoint
        if checkpoint_freq is not None and epoch % checkpoint_freq == 0:
            save_model_checkpoint(epoch=epoch,
                                  model_name=model_wrapper.model_name,
                                  number_of_classes=model_wrapper.number_of_classes,
                                  specs=specs,
                                  model_state=ema.ema.state_dict(),
                                  optimizer_state=optimizer.state_dict(),
                                  lr_scheduler_state=scheduler.lr_scheduler.state_dict(),
                                  output_dir=output_dir,
                                  model_file_name_prefix=str(epoch) + '_')

        final_epoch = epoch + 1 == number_of_epochs
        if epoch % eval_freq == 0 or final_epoch:
            # # If needed, make new incremental VOC evaluator every time validation runs.
            incremental_evaluator = IncrementalVocEvaluator(
                task_type == Tasks.IMAGE_OBJECT_DETECTION, len(val_index_map), val_iou_threshold
            ) if val_metric_type == ValidationMetricType.INCREMENTAL_VOC else None

            eval_bounding_boxes = validate(model=ema.ema, val_index_map=val_index_map,
                                           validation_loader=validation_loader,
                                           incremental_evaluator=incremental_evaluator, device=device,
                                           system_meter=valid_sys_meter, conf_thres=conf_thres,
                                           nms_iou_threshold=nms_iou_threshold,
                                           tile_predictions_nms_thresh=tile_predictions_nms_thresh,
                                           tiling_merge_predictions_time=tiling_merge_predictions_time,
                                           tiling_nms_time=tiling_nms_time)

            is_best = False
            if val_metric_type != ValidationMetricType.NONE:
                map_score = compute_metrics(eval_bounding_boxes, val_metric_type,
                                            val_coco_index, val_vocmap, incremental_evaluator,
                                            computed_metrics, per_label_metrics,
                                            coco_metric_time, voc_metric_time, primary_metric)

                # Tensorboard
                if tb_writer:
                    tb_writer.add_scalar("metrics/mAP_0.5", map_score, epoch)

                # start incrementing no progress counter only after early_stopping_delay
                if epoch >= early_stopping_delay:
                    no_progress_counter += 1

                if map_score > best_score:
                    no_progress_counter = 0

                if map_score >= best_score:
                    is_best = True
                    best_epoch = epoch
                    best_score = map_score
            else:
                logger.info("val_metric_type is None. Not computing metrics.")
                is_best = True
                best_epoch = epoch

            # save best model checkpoint
            if is_best:
                best_model_wts = copy.deepcopy(ema.ema.state_dict())
                save_model_checkpoint(epoch=best_epoch,
                                      model_name=model_wrapper.model_name,
                                      number_of_classes=model_wrapper.number_of_classes,
                                      specs=specs,
                                      model_state=best_model_wts,
                                      optimizer_state=optimizer.state_dict(),
                                      lr_scheduler_state=scheduler.lr_scheduler.state_dict(),
                                      output_dir=output_dir)

            logger.info("Current best primary metric score: {0:.3f} (at epoch {1})".format(round(best_score, 5),
                                                                                           best_epoch))

        # log to Run History every epoch with previously computed metrics, if not computed in the current epoch
        # to sync the metrics reported index with actual training epoch.
        if azureml_run is not None:
            utils.log_all_metrics(computed_metrics, azureml_run=azureml_run, add_to_logger=True)

        # measure elapsed time
        epoch_time.update(time.time() - epoch_end)
        epoch_end = time.time()
        mesg = "Epoch-level: [{0}]\t" \
               "Epoch-level Time {epoch_time.value:.4f} ({epoch_time.avg:.4f})".format(epoch, epoch_time=epoch_time)
        logger.info(mesg)

        if is_enabled_early_stopping and no_progress_counter > early_stopping_patience:
            logger.info("No progress registered after {0} epochs. "
                        "Early stopping the run.".format(no_progress_counter))
            break

        # collect garbage after each epoch
        gc.collect()

    # measure total training time
    train_time = time.time() - train_start
    utils.log_end_training_stats(train_time, epoch_time, train_sys_meter, valid_sys_meter)

    if log_verbose_metrics:
        utils.log_verbose_metrics_to_rh(train_time, epoch_time, train_sys_meter, valid_sys_meter, azureml_run)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    score_script_dir = os.path.join(os.path.dirname(current_dir), 'writers')
    write_scoring_script(output_dir=output_dir,
                         score_script_dir=score_script_dir,
                         task_type=task_type)

    write_per_label_metrics_file(output_dir, per_label_metrics, val_index_map)

    # this is to make sure the layers in ema can be loaded in the model wrapper
    # without it, the names are different (i.e. "model.0.conv.conv.weight" vs "0.conv.conv.weight")
    best_model_weights = {'model.' + k: v for k, v in best_model_wts.items()}

    write_artifacts(model_wrapper=model_wrapper,
                    best_model_weights=best_model_weights,
                    labels=model_wrapper.classes,
                    output_dir=output_dir,
                    run=azureml_run,
                    best_metric=best_score,
                    task_type=task_type,
                    device=device,
                    enable_onnx_norm=enable_onnx_norm,
                    model_settings=model_wrapper.model_settings.get_settings_dict(),
                    save_as_mlflow=save_as_mlflow,
                    is_yolo=True)


def _convert_all_targets_to_objects_per_image(all_targets, image_infos):
    all_targets = all_targets.detach().cpu().numpy()

    gt_objects_per_image = []

    # Go through the images and convert boxes/masks, labels and scores to format consumed by incremental evaluator.
    for i in range(len(image_infos)):
        # Make the mask for the objects in the current image.
        mask_current_image = all_targets[:, 0] == i

        # Get boxes and convert to pixel x1, y1, x2, y2 format.
        width, height = image_infos[i]["width"], image_infos[i]["height"]
        boxes = xywh2xyxy(all_targets[mask_current_image, 2:]) * np.array([[width, height, width, height]])
        unpad_bbox(boxes, (height, width), (image_infos[i]["pad"]))

        # Get classes.
        classes = all_targets[mask_current_image, 1]

        # Ground truth objects have boxes.
        gt_objects = {"boxes": boxes, "masks": None, "classes": classes, "scores": None}
        gt_objects_per_image.append(gt_objects)

    return gt_objects_per_image


def _convert_predictions_to_objects_per_image(predictions_per_image, image_infos):
    predicted_objects_per_image = []

    # Go through the images and convert the boxes/masks, labels and scores to format consumed by incremental evaluator.
    for i in range(len(image_infos)):
        # Get the predictions for the current image.
        predictions = predictions_per_image[i]

        if predictions is not None:
            # Convert predictions to NumPy.
            predictions = predictions.cpu().numpy()

            # Get boxes and clip to image size.
            boxes = predictions[:, :4]
            unpad_bbox(boxes, (image_infos[i]["height"], image_infos[i]["width"]), image_infos[i]["pad"])

            # Get classes and scores.
            classes = predictions[:, 5]
            scores = predictions[:, 4]

            # Predicted objects have boxes.
            predicted_objects = {"boxes": boxes, "masks": None, "classes": classes, "scores": scores}

        else:
            # No predictions for the current image.
            predicted_objects = {
                "boxes": np.zeros((0, 4)), "masks": None, "classes": np.zeros((0,)), "scores": np.zeros((0,))
            }

        predicted_objects_per_image.append(predicted_objects)

    return predicted_objects_per_image
