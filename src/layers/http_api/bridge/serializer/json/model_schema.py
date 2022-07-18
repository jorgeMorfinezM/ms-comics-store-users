"""This file has the purpose of serving to serialize a cat fact response to json format"""
from __future__ import annotations

from marshmallow import fields
from marshmallow import Schema


class ModelSchema(Schema):
    _id: fields.String()
    __v: fields.Integer()
    text: fields.String()
    updatedAt: fields.DateTime()
    deleted: fields.Boolean()

