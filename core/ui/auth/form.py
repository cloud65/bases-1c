# pylint: disable=line-too-long
"""Формы для авторизации"""
from typing import List

from fast_semaintic_ui.grid import GridColumn, Grid
from fast_semaintic_ui.enums import VerticalAlignEnum, ColorEnum, SizeEnum, TextAlignEnum
from fast_semaintic_ui.segment import Segment
from fast_semaintic_ui.event import EventSubmit, EventData
from fast_semaintic_ui.button import FormButton
from fast_semaintic_ui.form import Form, FormInput
from fast_semaintic_ui.elements import Value
from fast_semaintic_ui.event_sys import Favicon, EventSystem
from fast_semaintic_ui.header import Header
from fast_semaintic_ui.types import AnyElement


def get_system_data():
    """Возвращает настройки приложения для EventData"""
    icon = Favicon(url="/api/auth/img/auth.png")
    return EventSystem(
        title='Авторизация',
        lang='ru',
        icon=icon,
        style={'overflow': 'hidden'}
    )


class AuthSubmit(EventSubmit):
    """Авторизация"""
    url: str = '/auth/token'
    name: List[str] = ['auth']
    loading: str = 'loading_form'


def page_login() -> list[AnyElement]:
    """Окно авторизации"""
    user = FormInput(name='auth.username', fluid=True, focus=True,
                     icon='user', icon_position='left', placeholder='Логин')
    password = FormInput(name='auth.password', fluid=True,
                         icon='lock', icon_position='left',
                         placeholder='Пароль', type='password')

    button = FormButton(
        color=ColorEnum.teal, fluid=True, size=SizeEnum.large,
        content='Авторизация', icon='key', disabled=Value('login.disabled')
    )
    button.on_click = AuthSubmit()

    header = Header(h='h2', color=ColorEnum.blue, text_align=TextAlignEnum.center)
    header.text = 'Авторизация'
    form = Form(id='login_form', size=SizeEnum.large, loading=Value('loading_form'))

    form.add(Segment().add(user, password, button))

    column = GridColumn(style={'maxWidth': 450})
    column.add(header, form)

    grid = Grid(text_align=TextAlignEnum.center, vertical_align=VerticalAlignEnum.middle)
    grid.style = {'height': '100vh'}
    grid.add(column)
    return [grid, get_system_data(), EventData(data={'login.disabled': False})]
