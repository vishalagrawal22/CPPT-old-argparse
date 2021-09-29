import json

from werkzeug.serving import make_server
from parse import parse
from flask import Flask, jsonify, request, Response
app = Flask(__name__)

from werkzeug.serving import make_server

def shutdown():
    server.shutdown()

@app.route('/', methods=['POST'])
def get_data():
    data = request.json
    filename = data['name'].replace(' ', '').replace('.', '-')
    with open('{}.json'.format(filename), 'w') as json_file:
        json.dump(data, json_file)
    parse(data)
    shutdown()
    return Response(status=200)


if __name__ == '__main__':
    app.run(port=10043)
