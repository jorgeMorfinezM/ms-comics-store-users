'''This file intention is to provide serializer for CatFacts'''
from __future__ import annotations

from src.layers.domain.model.cat_facts_response import CatFactsResponse


class ModelSerializer:
    """This serializer has the purpose of setting requested dictionaries
        to domain object, in this case to a cat facts"""

    def __init__(self, response: dict):
        self.cat_facts_response = CatFactsResponse('', 0, '', '', True, '', 0)
        self.cat_facts_response._id = response['_id']
        self.cat_facts_response.__v = response['__v']
        self.cat_facts_response.text = response['text']
        self.cat_facts_response.updatedAt = response['updatedAt']
        self.cat_facts_response.deleted = response['deleted']
        self.cat_facts_response.source = response['source']
        self.cat_facts_response.sentCount = response['sentCount']
