"""Define functionality on service layer"""
from __future__ import annotations

from src.layers.persistence.utils.model_serializer import ModelSerializer
from src.layers.persistence.uow.model_uow import CatFactsUOW
from src.layers.services.exceptions import BaseCustomException
from src.layers.services.exceptions import IndexOutOfRange
from src.layers.services.exceptions import InvalidDictionaryFormat


class ModelService:

    def __init__(self, cat_facts_uow: CatFactsUOW):
        self.cat_facts_uow = cat_facts_uow

    def get_cat_facts(self, params):

        cat_facts_response = None

        if params is None:
            raise IndexOutOfRange('Fact parameter not is an integer number or is empty')

        response = self.cat_facts_uow.cat_facts_repository.get(params)

        if len(response) <= 0:
            raise BaseCustomException('Response is Empty, verify the API CatFacts endpoint on other service')

        try:

            cat_facts_response = [ModelSerializer(cat_fact).cat_facts_response for cat_fact in response
                                  if type(CatFactsResponseDictionary().__setitem__(1, cat_fact)) == dict]

            if cat_facts_response is not None:
                raise InvalidDictionaryFormat('Response does not have correct format')

        except InvalidDictionaryFormat as exc:
            print(exc)

        return cat_facts_response
