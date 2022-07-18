

'''This file intention is to provide repository for users'''
from __future__ import annotations

from src.layers.persistence.base_repository import AbstractRepository


class UserRepository(AbstractRepository):
    '''is an implementation of the abstract class of repository with cruds methods'''

    def __init__(self, session):
        self.session = session
        self.collection = self.session.user

    def add(self, model):
        self.collection.insert_one(model.__dict__)

    def get(self, reference):
        return self.collection.find_one(reference)

    def list_all(self):
        return list(self.collection.find())

    def update(self, model):
        self.collection.update_one({'uuid': model.uuid}, {'$set': model.__dict__})

    def delete(self, model):
        self.collection.delete_one({'uuid': model.uuid})
