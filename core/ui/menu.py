"""
Главная форма
"""

from typing import Union, List

from fastapi import APIRouter

from fast_semaintic_ui import FastSemanticUI, AnyEvent, Div
from fast_semaintic_ui.types import AnyElement

router = APIRouter()


@router.get("/", response_model=FastSemanticUI, response_model_exclude_none=True)
@router.get("/{menu}", response_model=FastSemanticUI, response_model_exclude_none=True)
async def main_page(menu: str = None) -> List[Union[AnyElement, AnyEvent]]:
    """Стартовая страница"""

    return Div(text='123')
