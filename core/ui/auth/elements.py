# pylint: disable=line-too-long, missing-class-docstring
"""Формы для авторизации"""
from typing import List, Any

from pydantic import Field

from fast_semaintic_ui.grid import GridColumn, Grid
from fast_semaintic_ui.enums import (
    VerticalAlignEnum, ColorEnum,
    SizeEnum, TextAlignEnum, PositionEnum
)
from fast_semaintic_ui.segment import Segment
from fast_semaintic_ui.event import EventSubmit
from fast_semaintic_ui.button import FormButton
from fast_semaintic_ui.form import Form, FormInput
from fast_semaintic_ui.elements import Value
from fast_semaintic_ui.event_sys import Favicon, EventSystem
from fast_semaintic_ui.header import Header


class SystemData(EventSystem):
    title: str = 'Авторизация'
    lang: str = 'ru'
    icon: Favicon = Favicon(url="/api/auth/img/auth.png")
    style: dict = {'overflow': 'hidden'}


class AuthSubmit(EventSubmit):
    """Авторизация"""
    url: str = '/auth/token'
    name: List[str] = ['auth']
    loading: str = 'loading_form'


class UserInput(FormInput):
    name: str = 'auth.username'
    fluid: bool = True
    focus: bool = True
    icon: str = 'user'
    icon_position: PositionEnum = PositionEnum.left
    placeholder: str = 'Логин'


class PasswordInput(FormInput):
    name: str = 'auth.password'
    fluid: bool = True
    icon: str = 'lock'
    icon_position: PositionEnum = PositionEnum.left
    placeholder: str = 'Пароль'
    type: str = 'password'


class AuthButton(FormButton):
    color: ColorEnum = ColorEnum.black
    fluid: bool = True
    size: SizeEnum = SizeEnum.large
    content: str = 'Авторизация'
    icon: str = 'key'
    disabled: bool = Value('login.disabled')
    on_click: AuthSubmit = Field(AuthSubmit(), serialization_alias='onClick')


class AuthHeader(Header):
    h: str =  Field('h2', serialization_alias='as')
    color: ColorEnum = ColorEnum.blue
    text_align: TextAlignEnum = TextAlignEnum.center
    text: str = 'Авторизация'


class AuthForm(Form):
    size: SizeEnum = SizeEnum.large
    loading: Value = Value('loading_form')
    children: List[Any] = [Segment().add(UserInput(), PasswordInput(), AuthButton())]


class AuthColumn(GridColumn):
    style: dict = {'maxWidth': 450}
    children: List[Any] = [AuthHeader(), AuthForm()]


class AuthWindow(Grid):
    text_align: TextAlignEnum = Field(TextAlignEnum.center, serialization_alias='textAlign')
    vertical_align: VerticalAlignEnum = Field(VerticalAlignEnum.middle, serialization_alias='verticalAlign')
    style: dict = {'height': '100vh'}
    children: List[Any] = [AuthColumn()]
