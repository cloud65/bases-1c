# pylint: disable=missing-class-docstring
"""
Элементы главной страницы
"""
from typing import Any, List

from pydantic import Field

from core.config import setting
from core.ui.auth.models import User
from core.ui.menu.submenu import SettingMenu
from fast_semaintic_ui.event import EventSystem
from fast_semaintic_ui.elements import Value
from fast_semaintic_ui.event_sys import Favicon
from fast_semaintic_ui.image import Image
from fast_semaintic_ui.segment import Segment
from fast_semaintic_ui.event import EventGoto, EventData
from fast_semaintic_ui.icon import Icon
from fast_semaintic_ui.simple import Div, Text
from fast_semaintic_ui.enums import PositionEnum, SizeEnum
from fast_semaintic_ui.menu import Menu, MenuItem

LOGO_URL = "/api/static/img/bases.png"


class SystemData(EventSystem):
    title: str = 'Списки ИБ'
    lang: str = 'ru'
    icon: Favicon = Favicon(url=LOGO_URL)
    style: dict = {'overflow': 'hidden'}


class AppVersion(Div):
    text: str = f'Version: {setting.version}'
    style: dict = {'color': 'green', 'position': 'absolute',
                   'bottom': '0.1em', 'left': '3em', 'fontSize': '0.8em'}


class UserData(EventData):
    def __init__(self, user: User):
        data = {'user.fullname': user.full_name or user.name}
        super().__init__(data=data)


class Logo(Image):
    size: SizeEnum = SizeEnum.mini
    src: str = LOGO_URL


class LogoItem(MenuItem):
    children: List[Any] = [Logo()]


class AppNameItem(MenuItem):
    header: bool = True
    text: str = 'Списки информационных баз'


class UsernameItem(Segment):
    content: Value = Value('user.fullname')
    basic: bool = True
    inverted: bool = True
    style: dict = {'margin': 'auto', 'color': '#e9c605', 'padding': 0}


class LogoutItem(MenuItem):
    children: List[Any] = [Icon(name='sign out'), Text('Выход')]
    position: PositionEnum = PositionEnum.right
    onClick: EventGoto = Field(EventGoto(url='/auth/logout'), serialization_alias='onClick')


class TopMenu(Menu):
    fixed: PositionEnum = PositionEnum.top
    inverted: bool = True
    style: dict = {'height': '3em'}
    children: List[Any] = [LogoItem(), AppNameItem(), UsernameItem(), LogoutItem()]


class LeftMenu(Menu):
    vertical: bool = True
    inverted: bool = True
    style: dict = {'borderRadius': 0, 'marginTop': '3em', 'marginBottom': 0}
    children: List[Any] = [SettingMenu(), AppVersion()]


class Content(Segment):
    basic: bool = True
    style: dict = {'display': 'flex', 'padding': 0,
                   'marginTop': '3em', 'flex': 1}
    children: List[Any] = [
        Div(id='content', style={'display': 'flex', 'flex': 1, 'margin': '2px'})
    ]


class Window(Div):
    style: dict = {'display': 'flex', 'height': '100vh'}
    children: List[Any] = [TopMenu(), LeftMenu(), Content()]

    def __init__(self, content):
        super().__init__()
        self.children[2].children[0].add(content)
