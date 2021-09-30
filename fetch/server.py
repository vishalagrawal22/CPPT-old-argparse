import os
import signal

from create.create_file import create_file
from flask import Flask, request, Response
app = Flask(__name__)

base_path = ""

@app.route('/', methods=['POST'])
def get_data():
    print("Retrieving problem data....")
    data = request.json
    create_file(base_path, data)
    os.kill(os.getpid(), signal.SIGINT)
    return Response(status = 200)  

def run_server(path):
    global base_path
    base_path = path
    app.run(port=10043)
