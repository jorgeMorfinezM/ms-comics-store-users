'''...'''
from __future__ import annotations

from datetime import datetime

from passlib.hash import pbkdf2_sha256 as sha256
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity)
from src.layers.domain.model.utils.encrypt_cryptography import encode
from src.layers.domain.model.utils.encrypt_cryptography import decode
from src.layers.http_api.bridge.serializer.json.user_schema import UserSchema
from src.layers.http_api.bridge.utils.formatter import json
from src.layers.domain.model.user import User
from src.layers.services.user_service import UserService


class UserRequestHandler:
    '''...'''

    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service
        self.user_schema = UserSchema()

    def number_of_users(self):
        '''...'''
        number_of_users = len(self.user_service.list_all_users())
        number_of_users_json = json.dumps({'number_of_users': number_of_users})
        return number_of_users_json

    def list_all_users(self):
        '''...'''
        # list[User]
        list_of_users = self.user_service.list_all_users()
        # list[{'..':'..', '..':'..'}]
        list_of_users = [self.user_schema.dump(company) for company in list_of_users]
        # '[{'..':'..', '..':'..'}]'
        list_of_users = json.dumps(list_of_users)
        return list_of_users

    def add_a_user(self, payload):
        '''...'''
        first_name, last_name = payload['first_name'], payload['last_name']
        phone, email = payload['phone'], payload['email'], username = payload['username']
        password = payload['password'], age = payload['age'], token = self.user_registration(payload['username'],
                                                                                             payload['password'])

        new_user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            phone=phone,
            _email=email,
            password=password,
            age=age,
            token=token.get('access_token'),
        )

        self.user_service.add_user(new_user)
        user_serializated = self.user_schema.dump(new_user)
        user_serializated = json.dumps(user_serializated)

        return user_serializated

    def get_a_user(self, payload):
        '''...'''
        username = payload['uuid']
        password = payload['password']

        domain_user = self.user_service.get_logged_user(username)
        user_serializated = self.user_schema.dump(domain_user)

        if password == decode(domain_user.password):
            user_serializated = json.dumps(user_serializated)

        return user_serializated

    def _update(self, user: User):
        '''...'''
        user.modified = datetime.now()
        user_updated = self.user_service.update_user(user)
        user_serializated = self.user_schema.dump(user_updated)
        user_serializated = json.dumps(user_serializated)
        return user_serializated

    def update_contact_info_for_a_user(self, payload):
        '''...'''
        first_name, last_name = payload['first_name'], payload['last_name']
        phone, email = payload['phone'], payload['email']
        uuid = payload['uuid']

        user_to_update = self.user_service.get_user(uuid)
        user_to_update.email = email
        user_to_update.first_name = first_name
        user_to_update.last_name = last_name
        user_to_update.set_phone_and_code_country(phone)

        return self._update(user_to_update)

    def list_users(self):
        '''...'''
        list_users = self.user_service.list_all_users()
        # list[{'..':'..', '..':'..'}]
        list_users = [self.user_schema.dump(user) for user in list_users]
        # '[{'..':'..', '..':'..'}]'
        list_users = json.dumps(list_users)
        return list_users

    def generate_hash(self, password):
        return sha256.hash(password)

    def verify_hash(self, password, hash_passwd):
        return sha256.verify(password, hash_passwd)

    def user_registration(self, username, password):
        response_login = None

        password_hash = self.generate_hash(password)

        try:

            if self.verify_hash(password, password_hash):

                access_token = create_access_token(identity=username)

                refresh_token = create_refresh_token(identity=username)

                response_login = json.dumps({
                    'access_token': access_token,
                    'refresh_token': refresh_token
                })

            else:
                response_login = json.dumps({
                    'error': 'Wrong credentials'
                })

        except Exception as error:
            raise error.args[0](
                'Wrong credentials or password not hashed: {}@{}'.format(
                    username, password
                )
            )

        return response_login
