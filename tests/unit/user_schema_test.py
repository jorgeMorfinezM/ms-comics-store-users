"""This file has the purpose of test users in json format"""
from __future__ import annotations

from src.layers.http_api.bridge.serializer.json.user_schema import UserSchema
from src.layers.http_api.bridge.utils.formatter import is_json
from src.layers.http_api.bridge.utils.formatter import json
from src.layers.domain.model.user import User


def make_users():
    """Fixture will generate users in memory"""
    return [
        User('jorgemm', 'jorge', 'morfinez', 34, 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
             2292706733, 'jorge.morfinez.m@gmail.com', 'jorgemm1345')
    ]


def test_user_in_json_format():
    """assert when a company has json format"""
    testeable_user = make_users()[0]  # In Prod env, please remove this little line for a uow.user.find({})
    user_json_schema = UserSchema()
    user_serializated = user_json_schema.dump(testeable_user)
    user_json = json.dumps(user_serializated, indent=2)

    assert is_json(user_json) is True


def test_list_of_users_in_json_format():
    """assert when a list of companies has json format"""

    user_json_schema = UserSchema()
    testeable_users = make_users()  # In Prod env, please remove this little line for a uow.user.list() or similar
    list_of_users = [user_json_schema.dump(user) for user in testeable_users]
    list_of_users_in_json_format = json.dumps(list_of_users, indent=2)

    assert is_json(list_of_users_in_json_format) is True
    assert len(testeable_users) == 2
