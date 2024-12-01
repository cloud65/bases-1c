# pylint: disable=missing-class-docstring
"""
Left menu items
"""
from pydantic import Field

from core.ui.menu.events import OnClickMenu, ActiveMenu
from fast_semaintic_ui import EventSubmit
from fast_semaintic_ui.elements import ClientFunction
from fast_semaintic_ui.menu import MenuItem, MenuHeader, MenuMenu


class SubMenuHeader(MenuHeader):
    content: str = "Настройки"


class UsersItem(MenuItem):
    id_menu: str = 'users'
    content: str = 'Пользователи'
    icon: str = 'users'
    active: ClientFunction = ActiveMenu()
    on_click: EventSubmit = Field(OnClickMenu('users'), serialization_alias='onClick')


class HostsItem(MenuItem):
    id_menu: str = 'hosts'
    content: str = 'Компьютеры'
    icon: str = 'computer'
    active: ClientFunction = ActiveMenu()
    on_click: EventSubmit = Field(OnClickMenu('hosts'), serialization_alias='onClick')


class SubItems(MenuMenu):
    children: list = [UsersItem(), HostsItem()]


class SettingMenu(MenuItem):
    children: list = [SubMenuHeader(), SubItems()]
