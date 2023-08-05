from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import os
import sys
import random
import logging
import alectiolite
from .init import init_experiment_, extract_config_
from .curate.classification import UniClassification as curate_classification
from .curate.object_detection import ObjectDetection as curate_object_detection
from .curate.object_segmentation import ObjectSegmentation as curate_object_segmentation
from .logger.logger import LoggerController, export_loop_logs, end_loop

__all__ = [
    "backend",
    "curate",
    "proto",
    "callbacks" "init_experiment_",
    "UniClassification",
    "ObjectDetection",
    "ObjectSegmentation",
    "LoggerController",
    "export_loop_logs",
    "end_loop",
]

__version__ = "0.0.1"


init = alectiolite.init_experiment_
experiment_config = alectiolite.extract_config_
curate_experiment = alectiolite.curate_classification
curate_object_detection = alectiolite.curate_object_detection
curate_object_segmentation = alectiolite.curate_object_segmentation
alectio_logger = alectiolite.LoggerController
export_loop_logs = alectiolite.export_loop_logs
end_loop = alectiolite.end_loop
