'''This file intention is to provide the custom domain exception
that limit the field of action of domain models and limit them to their bounded context
'''
from __future__ import annotations


class BaseCustomException(Exception):
    """Base custom exception"""


class InvalidDictionaryFormat(BaseCustomException):
    """Raised when dictionary object expected have malformed dictionary object format"""


class IndexOutOfRange(BaseCustomException):
    """Raised when number param requested not is an Integer data type"""
