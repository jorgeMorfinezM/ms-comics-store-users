'''Intention: provide CRUD methods and be injected in the uow'''
from __future__ import annotations

import abc


class AbstractRepository(abc.ABC):
    """Abstract class with the purpose of provide CRUD methods
    and be injected in the uow"""

    @abc.abstractmethod
    def get(self, params):
        """
        Get domain model

        :param: params: Arguments to parte on the requested endpoint.
        :return: Response model
        """
        raise NotImplementedError
