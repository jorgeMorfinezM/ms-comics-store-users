"""This file intention is to provide the custom domain exception
that limit the field of action of domain models and limit them to their bounded context
"""
from __future__ import annotations


class BaseCustomException(Exception):
    """Base custom exception"""
    ...


class IsNotModelError(BaseCustomException):
    """Raised when value it is not domain model"""
    ...
