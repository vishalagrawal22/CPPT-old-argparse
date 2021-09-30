import os
import sys

from fetch.server import run_server

app_name = "cppt"

def parse_manager(base_path):
    run_server(base_path)