import os
from .backend.backend_server import BackendServer


def init_experiment_(token):
    backend = BackendServer(token)
    exp_info = backend.init_backend()
    print("Initialized experiment")
    print("\n")


def extract_config_(token):
    backend = BackendServer(token)
    exp_info = backend.init_backend()
    return exp_info
