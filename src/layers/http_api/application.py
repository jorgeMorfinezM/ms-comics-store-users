from __future__ import annotations

from flask import Flask
from flask_cors import CORS
from config import HTTP_METHODS_ALLOW
from config import ORIGINS

from src.layers.http_api.endpoints.v1.user_view import endpoint_blueprint

app = Flask(__name__, instance_relative_config=True)

http_methods_allow = HTTP_METHODS_ALLOW
origins = ORIGINS

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
