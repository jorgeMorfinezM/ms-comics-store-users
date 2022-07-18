"""..."""
# mypy: ignore-errors
from __future__ import annotations

from flask_api import status
from flask import Blueprint
from flask import request
from flask import redirect
from src.layers.http_api.bridge.controller.user_request_handler import UserRequestHandler
from src.layers.persistence.uow.user_uow import UserUOW
from src.layers.services.user_service import UserService

endpoint_blueprint = Blueprint('users', __name__, url_prefix='/v1/users')


def _initialize():

    user_services = UserService(UserUOW())
    user_request_handler = UserRequestHandler(user_services)

    return user_request_handler


@endpoint_blueprint.post('/')
def add_new_users():
    """
    Add new user with data on the Body payload request
    """

    request_handler = _initialize()

    data = request.get_json(force=True)

    if not data or str(data) is None:
        return {'error': "Body doesn't exists in the request"}, status.HTTP_400_BAD_REQUEST

    response = request_handler.add_a_user(data)

    return response


@endpoint_blueprint.route('/logout/')
def logout():
    """
    User Logout endpoint
    """

    return redirect('/')


@endpoint_blueprint.get('/login/')
def login_user():

    request_handler = _initialize()

    username = request.args.get('username')
    password = request.args.get('password')

    payload = {
        "username": username,
        "password": password
    }

    response = request_handler.get_a_user(payload)

    return response
