'''Intention: Manage engine db clients'''
from __future__ import annotations

import abc


class AbstractUnitOfWork(abc.ABC):
    """Abstract class with the purpose of manage engine db clients"""

    @abc.abstractmethod
    def __enter__(self, **kwargs):
        """Make a database connection and return it"""
        raise NotImplementedError
