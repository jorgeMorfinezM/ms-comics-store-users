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