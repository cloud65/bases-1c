# pylint: disable=missing-class-docstring
"""
Events Main Menu
"""
from typing import List

from fast_semaintic_ui.elements import ClientFunction
from fast_semaintic_ui.event import EventSubmit


class ActiveMenu(ClientFunction):
    fields: List[str] = ['active']
    code: str = 'return component.id_menu===data["menu.active"]'


class OnClickMenu(EventSubmit, extra='forbid'):
    full_loading: bool = True
    method: str = 'get'

    def __init__(self, name: str):
        super().__init__(url=f'/content/{name}')
