import os
import json
import errno
import boto3
import pickle
import pickletools
import numpy as np
from alectiolite.metrics.classification import ClassificationMetrics
from alectiolite.metrics.object_detection import Metrics, batch_to_numpy
from rich.console import Console
from alectiolite.backend.s3_client import S3Client
from alectiolite.backend.sql_client import *


__all__ = ["ALPickleOps"]

console = Console(style="green", record=True)


class ALPickleOps(object):
    def __init__(self, backend_config):
        self.backend_config = backend_config
        self.client = S3Client()

    def experiment_pickle_logger(self, monitor, data, config):
        """
        Used by users to log experiment level logs
        #TODO replace/adapt with framework based callbacks

        """

        if monitor == "datasetstate" and self.backend_config.CUR_LOOP == "":
            filename = os.path.join(
                self.backend_config.EXPERIMENT_DIR, "data_map.pkl"
            ).replace("\\", "/")
            self._log_pickle(monitor, filename, data)
        elif monitor == "datasetstate" and self.backend_config.CUR_LOOP >= 0:
            filename = os.path.join(
                self.backend_config.EXPERIMENT_DIR, "data_map.pkl"
            ).replace("\\", "/")
            self._log_pickle(monitor, filename, data)
        ## Read meta file
        elif (
            monitor == "meta"
        ):  # TODO when streaming is available people may add classes on the fly
            filename = os.path.join(
                self.backend_config.PROJECT_DIR, "meta.json"
            ).replace("\\", "/")
            self._log_json(monitor, filename, data)

        ## Read selected indices
        elif monitor == "selected_indices" and self.backend_config.CUR_LOOP == "":
            filename = os.path.join(
                self.backend_config.EXPERIMENT_DIR, "selected_indices.pkl"
            ).replace("\\", "/")
            labeled = self._log_pickle(monitor, filename, data, mode="read")
            self._log_pickle(monitor, filename, labeled)
        elif monitor == "selected_indices" and self.backend_config.CUR_LOOP >= 0:
            labeled = []
            file_selected = os.path.join(
                self.backend_config.EXPERIMENT_DIR,
                "selected_indices.pkl",
            ).replace("\\", "/")
            for loop in range(int(self.backend_config.CUR_LOOP) + 1):
                filename = os.path.join(
                    self.backend_config.EXPERIMENT_DIR,
                    "selected_indices_{}.pkl".format(loop),
                ).replace("\\", "/")
                labeled.extend(self._log_pickle(monitor, filename, data, mode="read"))
            print("labeled length: ", len(labeled))
            self._log_pickle(monitor, file_selected, labeled)

        ## Train insights
        elif monitor == "insights" and self.backend_config.CUR_LOOP == "":
            filename = os.path.join(
                self.backend_config.EXPERIMENT_DIR, "insights.pkl"
            ).replace("\\", "/")
            train_insights = self._train_insights(data)

            self._log_pickle(monitor, filename, train_insights)
            self._sweep_experiment(monitor, filename)
        elif monitor == "insights" and self.backend_config.CUR_LOOP >= 0:
            filename = os.path.join(
                self.backend_config.EXPERIMENT_DIR,
                "insights_{}.pkl".format(self.backend_config.CUR_LOOP),
            ).replace("\\", "/")
            train_insights = self._train_insights(data)

            self._log_pickle(monitor, filename, train_insights)
            self._sweep_experiment(monitor, filename)

        ## Infer logits
        elif monitor == "logits" and self.backend_config.CUR_LOOP == "":
            if "classification" in self.backend_config.TYPE:
                filename = os.path.join(
                    self.backend_config.EXPERIMENT_DIR, "logits.pkl"
                ).replace("\\", "/")
                self._remap_outs(data)
                self._log_pickle(monitor, filename, data)
                self._sweep_experiment(monitor, filename)
            elif "object_detection" in self.backend_config.TYPE:
                database = os.path.join(self.backend_config.EXPERIMENT_DIR, 'infer_outputs.db')
                conn = create_database(database)
                remapped_data = self._remap_outs(data)
                for k, v in remapped_data.items():
                    add_index(conn, k, v)
                conn.close()
                self._sweep_experiment(monitor, database)
        elif monitor == "logits" and self.backend_config.CUR_LOOP >= 0:
            if "classification" in self.backend_config.TYPE:
                filename = os.path.join(
                    self.backend_config.EXPERIMENT_DIR,
                    "logits_{}.pkl".format(self.backend_config.CUR_LOOP),
                ).replace("\\", "/")
                remapped_data = self._remap_outs(data)
                log_data = {}
                for k, v in remapped_data.items():
                    log_data[k] = {monitor: v}
                self._log_pickle(monitor, filename, log_data)
                self._sweep_experiment(monitor, filename)
            elif "object_detection" in self.backend_config.TYPE:
                database = os.path.join(self.backend_config.EXPERIMENT_DIR, 'infer_outputs_{}.db'.format(self.backend_config.CUR_LOOP))
                conn = create_database(database)
                remapped_data = self._remap_outs(data)
                for k, v in remapped_data.items():
                    add_index(conn, k, v)
                conn.close()
                self._sweep_experiment(monitor, database)

        ## Test metrics
        elif monitor == "metrics" and self.backend_config.CUR_LOOP == "":
            filename = os.path.join(
                self.backend_config.EXPERIMENT_DIR, "metrics.pkl"
            ).replace("\\", "/")
            experiment_meta = json.load(
            open(
                os.path.join(self.backend_config.PROJECT_DIR, "meta.json").replace(
                    "\\", "/"
                ),
                "rb",
                )
            )
            if (
                self.backend_config.TYPE == "text_classification"
                or self.backend_config.TYPE == "image_classification"
            ):
                m = ClassificationMetrics(data["predictions"], data["labels"], data["logits"])

                metrics = {
                    "accuracy": m.get_accuracy(),
                    "f1_score_per_class": m.get_f1_score_per_class(),
                    "f1_score": m.get_f1_score(),
                    "precision_per_class": m.get_precision_per_class(),
                    "precision": m.get_precision(),
                    "recall_per_class": m.get_recall_per_class(),
                    "recall": m.get_recall(),
                    "confusion_matrix": m.get_confusion_matrix(),
                    "acc_per_class": m.get_acc_per_class(),
                    "label_disagreement": m.get_label_disagreement(),
                    "mean_confidence": m.get_mean_confidence()
                }
            elif self.backend_config.TYPE == "2d_object_detection":
                det_boxes, det_labels, det_scores, true_boxes, true_labels = batch_to_numpy(
                    data["predictions"], data["labels"]
                )

                m = Metrics(
                    det_boxes=det_boxes,
                    det_labels=det_labels,
                    det_scores=det_scores,
                    true_boxes=true_boxes,
                    true_labels=true_labels,
                    num_classes=len(experiment_meta["class_labels"]),
                )

                metrics = {
                    "mAP": m.getmAP(),
                    "AP": m.getAP(),
                    "precision": m.getprecision(),
                    "recall": m.getrecall(),
                    "confusion_matrix": m.getCM().tolist(),
                    "class_labels": experiment_meta["class_labels"],
                }
            self._log_pickle(monitor, filename, metrics)
            self._sweep_experiment(monitor, filename)
        elif monitor == "metrics" and self.backend_config.CUR_LOOP >= 0:
            experiment_meta = json.load(
            open(
                os.path.join(self.backend_config.PROJECT_DIR, "meta.json").replace(
                    "\\", "/"
                ),
                "rb",
                )
            )
            filename = os.path.join(
                self.backend_config.EXPERIMENT_DIR,
                "metrics_{}.pkl".format(self.backend_config.CUR_LOOP),
            ).replace("\\", "/")
            if (
                self.backend_config.TYPE == "text_classification"
                or self.backend_config.TYPE == "image_classification"
            ):
                print("logging metrics!!!!")
                m = ClassificationMetrics(data["predictions"], data["labels"], data["logits"])

                metrics = {
                    "accuracy": m.get_accuracy(),
                    "f1_score_per_class": m.get_f1_score_per_class(),
                    "f1_score": m.get_f1_score(),
                    "precision_per_class": m.get_precision_per_class(),
                    "precision": m.get_precision(),
                    "recall_per_class": m.get_recall_per_class(),
                    "recall": m.get_recall(),
                    "confusion_matrix": m.get_confusion_matrix(),
                    "acc_per_class": m.get_acc_per_class(),
                    "label_disagreement": m.get_label_disagreement(),
                    "mean_confidence": m.get_mean_confidence()
                }
            elif self.backend_config.TYPE == "2d_object_detection":
                det_boxes, det_labels, det_scores, true_boxes, true_labels = batch_to_numpy(
                    data["predictions"], data["labels"]
                )

                m = Metrics(
                    det_boxes=det_boxes,
                    det_labels=det_labels,
                    det_scores=det_scores,
                    true_boxes=true_boxes,
                    true_labels=true_labels,
                    num_classes=len(experiment_meta["class_labels"]),
                )

                metrics = {
                    "mAP": m.getmAP(),
                    "AP": m.getAP(),
                    "precision": m.getprecision(),
                    "recall": m.getrecall(),
                    "confusion_matrix": m.getCM().tolist(),
                    "class_labels": experiment_meta["class_labels"],
                }
            self._log_pickle(monitor, filename, metrics)
            self._sweep_experiment(monitor, filename)
        else:
            raise ValueError(
                "Invalid experiment loop and/or monitor value chosen to monitor"
            )

    def _train_insights(self, data):
        if "labels" in data:
            labels = data["labels"]
            unique, counts = np.unique(labels, return_counts=True)
            num_queried_per_class = {u: c for u, c in zip(unique, counts)}
            insights = {
                "train_time": data["train_time"],
                "num_queried_per_class": num_queried_per_class,
            }
        else:
            insights = {
                "train_time": data["train_time"]}
        return insights

    def _log_pickle(self, monitor, filename, data, mode="write"):
        if mode == "write":
            with open(filename, "wb") as f:
                pickled = pickle.dumps(data)
                optimized_pickle = pickletools.optimize(pickled)
                f.write(optimized_pickle)
                console.print(
                    "Successfully logged {} for your current loop at {}".format(
                        monitor, filename
                    )
                )
        elif mode == "read":
            selected = self.client.read(
                self.backend_config.BUCKET_NAME,
                object_key=filename,
                file_format="pickle",
            )
            self._log_pickle(monitor, filename, selected, mode="write")
            return selected
            # self._log_pickle(monitor, filename, selected, mode="write")

        else:
            raise ValueError("Invalid read/write mode set")

    def _log_json(self, monitor, filename, data):
        # Usually read
        s3 = self.client.lite_session.resource("s3")
        bucket = s3.Bucket(self.backend_config.BUCKET_NAME)
        json_load_s3 = lambda f: json.load(bucket.Object(key=f).get()["Body"])
        meta_data = json_load_s3(filename)
        with open(filename, "w") as f:
            json.dump(meta_data, f)

    def _remap_outs(self, data):
        experiment_meta = json.load(
            open(
                os.path.join(self.backend_config.PROJECT_DIR, "meta.json").replace(
                    "\\", "/"
                ),
                "rb",
            )
        )
        train_size = list(range(experiment_meta["train_size"]))

        selected_file = self.load_pickle(
            os.path.join(
                self.backend_config.EXPERIMENT_DIR, "selected_indices.pkl"
            ).replace("\\", "/")
        )
        # print("selected_file" , selected_file)

        unselected = sorted(list(set(train_size) - set(selected_file)))

        # Remap to absolute indices
        remap_outputs = {}
        for i, (k, v) in enumerate(data.items()):
            ix = unselected.pop(0)
            remap_outputs[ix] = v
        return remap_outputs

    def _sweep_experiment(self, monitor, filename):
        if not os.path.isfile(filename):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filename)

        for f in os.listdir(self.backend_config.PROJECT_DIR):
            if "meta" not in f:
                if not os.path.isdir(os.path.join(self.backend_config.PROJECT_DIR, f)):
                    self.client.multi_part_upload_file(
                        os.path.join(self.backend_config.PROJECT_DIR, f).replace(
                            "\\", "/"
                        ),
                        self.backend_config.BUCKET_NAME,
                        os.path.join(self.backend_config.PROJECT_DIR, f).replace(
                            "\\", "/"
                        ),
                    )

        for f in os.listdir(self.backend_config.EXPERIMENT_DIR):
            if "meta" not in f:
                if not os.path.isdir(
                    os.path.join(self.backend_config.EXPERIMENT_DIR, f).replace(
                        "\\", "/"
                    )
                ):
                    self.client.multi_part_upload_file(
                        os.path.join(self.backend_config.EXPERIMENT_DIR, f).replace(
                            "\\", "/"
                        ),
                        self.backend_config.BUCKET_NAME,
                        os.path.join(self.backend_config.EXPERIMENT_DIR, f).replace(
                            "\\", "/"
                        ),
                    )

    def load_pickle(self, filename):
        pickle_file = pickle.load(open(filename, "rb"))
        return pickle_file
