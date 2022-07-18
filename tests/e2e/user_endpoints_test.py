from __future__ import annotations

import json

from src.layers.http_api.application import app
from src.layers.http_api.bridge.controller.user_request_handler import UserRequestHandler
from src.layers.http_api.endpoints.v1 import user_view
from src.layers.persistence.uow.user_uow import UserUOW
from src.layers.services.user_service import UserService


def init_services(mongodb):
    user_service = UserService(UserUOW(mongodb))
    user_view.user_request_handler = UserRequestHandler(user_service)


def test_user_add_view_happy_path(mongodb):

    init_services(mongodb)

    payload = {
        "username": "jorgemm13",
        "first_name": "Jorge",
        "last_name": "Mojica",
        "age": 34,
        "phone": 2292706733,
        "email": "jorge.morfinez.m@gmail.com",
        "password": "jorgemm13081054"
    }

    response = app.test_client().post(
        '/v1/users/',
        data=json.dumps(payload),
        content_type='application/json',
    )

    user_created = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 201
    assert user_created['email'] == 'jorge.morfinez.m@gmail.com'
    assert user_created['username'] == 'jorgemm13'
    assert user_created['phone'] == '+2292706733'
    assert user_created['is_active'] is True


def test_get_a_user(mongodb):

    init_services(mongodb)

    response = app.test_client().get('/v1/users/login/?username=jorgemm13&password=jorgemm13081054')

    company = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert company['email'] == 'jorge.morfinez.m@gmail.com'
    assert company['username'] == 'jorgemm13'
    assert company['phone'] == '2292706733'
    assert company['is_active'] is True
