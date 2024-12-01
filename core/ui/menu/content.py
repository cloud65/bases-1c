# pylint: disable=missing-class-docstring
"""
Контент главного меню
"""
from core.ui.table_view.components import TableView


class Content(TableView):
    def __init__(self, menu: str):
        super().__init__(title = menu)
