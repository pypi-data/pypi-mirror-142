from __future__ import print_function

import grpc

import os
import time
import requests
import logging
from tqdm import tqdm
from tqdm import trange
from rich.console import Console
from rich.table import Table
from ..config import backend_config
from ..config import update_backend_config

# import bidirectional_pb2_grpc as bidirectional_pb2_grpc
# from .bidirectional_pb2_grpc import Bidirectional, BidirectionalStub , BidirectionalServicer
# import alectiolite.bidirectional_pb2 as bidirectional_pb2

import alectiolite.proto.bidirectional_pb2_grpc as bidirectional_pb2_grpc
import alectiolite.proto.bidirectional_pb2 as bidirectional_pb2


__all__ = [
    "BackendServer",
]

console = Console(style="bold yellow")


class BackendServer(object):
    def __init__(self, token):
        logging.info("Triggering Alectio jobs with your experiment token ", token)
        self.token = token

    def _printexperimentinfo(self, payload):

        table = Table(show_header=True, header_style="bold magenta")
        console.print("\n")
        console.print("Details of your experiment ... ")
        rowstrings = ""

        for k, v in payload.items():
            table.add_column(str(k), justify="center")
            rowstrings + str(v) + ","

        table.add_row(rowstrings)
        console.print(table)

    def init_backend(self, verbose=False):
        logging.info("Triggering task ...")
        self.payload = self._triggertask()
        if verbose:
            self._printexperimentinfo(self.payload)
        return self.payload

    def _triggertask(self):
        currtime = 0
        waittime = 40  # wait time approximately 10 minutes
        ping_server = ["Request {}".format(n) for n in range(waittime)]
        backend_ip = backend_config.BACKEND_IP
        url = "".join(["http://", backend_ip, ":{}".format(backend_config.PORT)])
        exp_URL = "".join([url, backend_config.EXP_URL])
        sdk_response_URL = "".join([url, backend_config.SDK_RESPONSE_URL])
        response = requests.post(url=exp_URL, json={"exp_token": self.token})
        exp_response = response.json()["message"]
        if exp_response == "Started":
            with console.status(
                "[bold green] Triggering Alectio servers ..."
            ) as status:
                while True:
                    # Calling Backend Servers
                    response_child = requests.post(
                        url=sdk_response_URL, json={"exp_token": self.token}
                    )
                    # response_child = self.getSDKResponse()
                    if response_child.json()["status"] == "Fetched":
                        ping = ping_server.pop(0)
                        console.print("{} succeeded".format(ping))
                        console.print(
                            "Setting up curation , hold tight while we crunch some numbers"
                        )
                        return response_child.json()
                    if response_child.json()["status"] == "Finished":
                        if int(response_child.json()["cur_loop"]) < int(
                            response_child.json()["n_loop"]
                        ):
                            console.print(
                                "Server retriggering experiment creation process for token {}... ".format(
                                    self.token
                                )
                            )
                            continue
                        print("Experiment complete")
                        os.environ["AWS_ACCESS_KEY_ID"] = " "
                        os.environ["AWS_SECRET_ACCESS_KEY"] = " "
                        break
                    if response_child.json()["status"] == "Failed":
                        ping = ping_server.pop(0)
                        time.sleep(10)
                        console.print("{} failed. Retrying ...".format(ping))
                    if not ping_server:
                        console.print(
                            "Sorry out servers are offline, try again later !"
                        )
                        break
        else:
            console.print(
                "Your experiment could not be created, Check your token or try retriggering the experiment !"
            )
