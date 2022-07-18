from __future__ import annotations

from flask import Flask
from flask_cors import CORS

from src.layers.http_api.endpoints.v1.view import endpoint_blueprint

app = Flask(__name__, instance_relative_config=True)

POST = 'POST'
GET = 'GET'
PATCH = 'PATCH'
DELETE = 'DELETE'

http_methods_allow = [POST, GET, PATCH, DELETE]
origins = ['localhost']

CORS(
    app, resources={r'/v1/*'},
    origins=origins,
    methods=http_methods_allow,
    supports_credentials=True,
    vary_header=True,
)

app.register_blueprint(endpoint_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
