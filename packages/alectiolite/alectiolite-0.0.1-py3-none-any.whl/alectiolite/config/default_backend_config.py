from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os
from yacs.config import CfgNode as CN

_C = CN()

# Backend configs
_C.SANDBOX_BUCKET = ""
_C.BACKEND_IP = "sdk.alectio.com"
_C.PORT = 80
_C.EXP_URL = "/api/v0/start_experiment_response"
_C.SDK_RESPONSE_URL = "/api/v0/get_sdk_response"


# Experiment configs
_C.STATUS = ""
_C.EXPERIMENT_ID = ""
_C.PROJECT_ID = ""
_C.CUR_LOOP = 0
_C.USER_ID = ""
_C.BUCKET_NAME = ""
_C.TYPE = ""
_C.N_REC = 0
_C.N_LOOP = 0


# File configs
_C.OUTFILES = (
    "metrics",
    "train_predictions",
    "train_ground_truth",
    "test_predictions",
    "test_ground_truth",
    "datasetstate",
    "logits",
    "boxes" "endloop",
    "insights",
)
_C.INFILES = ("meta", "labeled_pool", "selected_indices")
_C.OUT_FORMAT = "pickle"
_C.DB_INIT = False

# Log directories
_C.EXPERIMENT_DIR = ""
_C.PROJECT_DIR = ""
_C.CLOUD_ACCESS_API = "http://prodbackend.alectio.com/experiments/getcredentials"


def update_backend_config(cfg, include_cfg):
    cfg.defrost()
    cfg.merge_from_list(include_cfg)
    cfg.freeze()


if __name__ == "__main__":
    import sys

    with open(sys.argv[1], "w") as f:
        print(_C, file=f)
