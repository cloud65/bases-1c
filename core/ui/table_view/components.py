# pylint: disable=missing-class-docstring, line-too-long
"""
ModelView Components
"""
from typing import Any, List

from pydantic import Field

from fast_semaintic_ui.button import Button
from fast_semaintic_ui.icon import Icon
from fast_semaintic_ui.simple import Text
from fast_semaintic_ui.header import Header
from fast_semaintic_ui.segment import SegmentGroup, Segment
from fast_semaintic_ui.enums import ColorEnum


class ButtonReload(Button):
    icon: str = 'sync'
    color: ColorEnum = ColorEnum.green
    basic: bool = True
    popup: str = "Reload table"


class ButtonAdd(Button):
    icon: str = 'plus'
    color: ColorEnum = ColorEnum.blue
    basic: bool = True
    popup: str = "Add row"
    style: dict = {'marginLeft': '2em'}


class ButtonCopy(Button):
    icon: str = 'copy outline'
    color: ColorEnum = ColorEnum.blue
    basic: bool = True
    popup: str = "Copy row"


class ButtonEdit(Button):
    icon: str = 'pencil'
    color: ColorEnum = ColorEnum.blue
    basic: bool = True
    popup: str = "Edit row"


class ButtonRemove(Button):
    icon: str = 'trash'
    color: ColorEnum = ColorEnum.red
    basic: bool = True
    popup: str = "Remove row"
    style: dict = {'marginLeft': '4em'}


class TableView(SegmentGroup):
    style: dict = {'flex': '1', 'display': 'flex',
                   'flexDirection': 'column', 'border': 'none'}
    icon: Icon = Field(Icon('file'), exclude=True)
    title: str = Field('Table', exclude=True)
    commands: List[Any] = Field(
        [
            ButtonReload(),
            ButtonAdd(), ButtonCopy(), ButtonEdit(),
            ButtonRemove()
        ],
        exclude=True
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        title = Segment(style={'margin': '.2em'})
        header = Header()
        header.add(self.icon)
        header.add(Text(self.title))
        title.add(header)
        self.add(title)
        if self.commands:
            self.add(Segment(style={'padding': '0.3em 0.5em'}).add(*self.commands))
        self.add(Segment(style={'display': 'flex', 'flexGrow': 1, 'padding': 0, 'borderTop': 'none'}))
