'''This file intention is to provide serializer for user'''
from __future__ import annotations

from src.layers.domain.model.user import User


class UserSerializer:
    '''This serializer has the purpose of setting mongo dictionaries
    to domain objects, in this case to a user'''

    def __init__(self, mongo_user: dict):

        self.user = User(
            'username_template', 'first_name_template', 'last_name_template', 18,
            'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 5555555555, 'email_template@gmail.com',
            'password_template',
        )

        self.user.id = mongo_user['uuid']
        self.user.username = mongo_user['username']
        self.user.first_name = mongo_user['first_name']
        self.user.last_name = mongo_user['last_name']
        self.user.age = mongo_user['age']
        self.user.token = mongo_user['token']
        self.user.phone = mongo_user['phone']
        self.user.phone_country_code = mongo_user['phone_country_code']
        self.user._email = mongo_user['_email']
        self.user.password = mongo_user['password']
        self.user.created = mongo_user['created']
        self.user.modified = mongo_user['modified']
        self.user.is_active = mongo_user['is_active']
