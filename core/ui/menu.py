"""
Главная форма
"""

from typing import Union, List, Annotated

from fastapi import APIRouter, Depends

from core.ui.auth.core import get_current_active_user
from core.ui.auth.models import User, credentials_exception
from fast_semaintic_ui import FastSemanticUI, AnyEvent, Div
from fast_semaintic_ui.types import AnyElement

router = APIRouter()


@router.get("/", response_model=FastSemanticUI, response_model_exclude_none=True)
@router.get("/{menu}", response_model=FastSemanticUI, response_model_exclude_none=True)
async def main_page(
        user: Annotated[User, Depends(get_current_active_user)],
        menu: str = None,
) -> List[Union[AnyElement, AnyEvent]]:
    """Стартовая страница"""

    if user is None:
        raise credentials_exception


    return Div(text='123')
