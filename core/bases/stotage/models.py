# pylint: disable=missing-function-docstring, unused-argument, missing-class-docstring
"""
Описание моделей
"""
from enum import IntEnum
from uuid import uuid4

from peewee import Model, UUIDField, CharField, IntegerField


class UserRight(IntEnum):
    ADMIN = 1
    USER = 2


class UUIDMixin(Model):
    id = UUIDField(primary_key=True, default=uuid4)


class Users(UUIDMixin):
    name = CharField(max_length=20, index=True)
    full_name = CharField(max_length=200, null=True)
    right = IntegerField(default=2, choices=UserRight)


class Groups(UUIDMixin):
    name = CharField(max_length=50, index=True)


class Hosts(UUIDMixin):
    ip = CharField(max_length=15, index=True)
    name = CharField(max_length=50, index=True)


class Infobases(UUIDMixin):
    name = CharField(max_length=50, index=True)
    ref = CharField(max_length=50)
    server = CharField(max_length=50)
    port = IntegerField(null=True)


def bind_models(db):
    models = [Users, Groups, Hosts, Infobases]
    for model in models:
        model.bind(db)
        model.create_table()
