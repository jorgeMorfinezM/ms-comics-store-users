"""Intention: setup client connection to be injected in Request API"""
from __future__ import annotations

import abc


class Config(abc.ABC):
    """Abstract class with the purpose of setup client
    connection"""

    @abc.abstractmethod
    def __init__(self, url_host, endpoint, http_method, headers):
        """This constructor have the capability setup
        connection without engine"""
        raise NotImplementedError


class APIConnect(abc.ABC):
    """Abstract class with the purpose of Connect to a api client"""

    @abc.abstractmethod
    def __init__(self, config: Config):
        raise NotImplementedError

    @abc.abstractmethod
    def request(self, params):
        """initialize connection or session to api client"""
        raise NotImplementedError
