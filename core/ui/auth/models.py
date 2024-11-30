# pylint: disable=missing-class-docstring
"""
Описание моделей для авторизации
"""

from typing import Union

from pydantic import BaseModel, ConfigDict

from fast_semaintic_ui.auth import AuthRedirect

credentials_exception = AuthRedirect('/auth/login')

class AuthData(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True)
    name: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None
