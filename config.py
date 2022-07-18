from __future__ import annotations

from decouple import config as env

FLASK_SECRET_KEY = env('FLASK_SECRET_KEY')
# Directory to en-route the flask application and config
FLASK_APP = env('FLASK_APP')

FLASK_RUN_PORT = env('FLASK_RUN_PORT')

# Flask API web framework working environment
FLASK_ENV = env('FLASK_ENV')
# The environment, can be: "local", "test", "producccion"
ENVIRONMENT = env('ENVIRONMENT')

FERNET_SECRET_KEY = env('FERNET_SECRET_KEY')

HEADERS = env('HEADERS')

HTTP_METHODS_ALLOW = env('HTTP_METHODS_ALLOW')
ORIGINS = env('ORIGINS')

# Database Envs
DB_NAME = env('DB_NAME')
DB_ROOT_USERNAME = env('DB_ROOT_USERNAME')
DB_ROOT_PASSWORD = env('DB_ROOT_PASSWORD')
MONGODB_HOST = env('MONGODB_HOST')
MONGODB_PORT = env('MONGODB_PORT')
MONGO_CLUSTER_CONN = env('MONGO_CLUSTER_CONN')
