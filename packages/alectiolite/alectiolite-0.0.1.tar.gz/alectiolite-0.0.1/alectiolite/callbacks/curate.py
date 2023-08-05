import alectiolite
import duckdb
import time
import pickle
import os
import json
from rich.console import Console
from ..config import backend_config
from alectiolite.callbacks import AlectioCallback


class CurateCallback(AlectioCallback):
    def __init__(self):
        self.alectio_database = duckdb.connect(database=":memory:", read_only=False)

    def on_project_start(self, monitor, data, config):
        # Alectio controlled
        # Override only if you need to under your circumstance
        alectiolite.LoggerController(
            monitor=monitor, data=None, config=config, alectio_db=self.alectio_database
        )

    def on_experiment_start(self, monitor, data, config):
        alectiolite.LoggerController(
            monitor=monitor, data=data, config=config, alectio_db=self.alectio_database
        )

    def on_train_start(self, monitor, config, data=None):
        self.start_time = time.time()
        alectiolite.LoggerController(
            monitor=monitor, data=data, config=config, alectio_db=self.alectio_database
        )
        filename = open(
            os.path.join(backend_config.EXPERIMENT_DIR, "selected_indices.pkl").replace(
                "\\", "/"
            ),
            "rb",
        )
        indices = pickle.load(filename)
        filename.close()
        return indices

    def on_train_end(self, monitor, config, data=None):
        if data is not None:
            data["train_time"] = time.time() - self.start_time
        else:
            data = {}
            data["train_time"] = time.time() - self.start_time
        alectiolite.LoggerController(
            monitor=monitor, data=data, config=config, alectio_db=self.alectio_database
        )

    def on_test_start(self, monitor, data, config):
        # Alectio controlled
        # Override only if you need to under your circumstance
        alectiolite.LoggerController(
            monitor=monitor, data=None, config=config, alectio_db=self.alectio_database
        )

    def on_test_end(self, monitor, data, config):
        alectiolite.LoggerController(
            monitor=monitor, data=data, config=config, alectio_db=self.alectio_database
        )

    def on_infer_start(self, monitor=None, data=None, config=None):
        with open(
            os.path.join(backend_config.PROJECT_DIR, "meta.json").replace("\\", "/")
        ) as f:
            meta = json.load(f)
        with open(
            os.path.join(backend_config.EXPERIMENT_DIR, "selected_indices.pkl").replace(
                "\\", "/"
            ),
            "rb",
        ) as f:
            labeled = pickle.load(f)
        ts = range(meta["train_size"])
        unlabeled = sorted(list(set(ts) - set(labeled)))
        return unlabeled
        # alectiolite.LoggerController(
        #     monitor=monitor, data=data, config=config, alectio_db=self.alectio_database
        # )

    def on_infer_end(self, monitor, data, config):

        alectiolite.LoggerController(
            monitor=monitor, data=data, config=config, alectio_db=self.alectio_database
        )

    def on_process_end(self, token):
        alectiolite.export_loop_logs(alectio_db=self.alectio_database, token=token)

    def on_experiment_end(self, token):
        return alectiolite.end_loop(token=token)
