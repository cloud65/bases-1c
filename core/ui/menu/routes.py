"""
Главное меню
"""
from typing import Union, Any, Annotated

from fastapi import APIRouter, Depends

from core.ui.auth.core import get_current_active_user
from core.ui.auth.models import User
from core.ui.menu.elements import Window, UserData, SystemData
from fast_semaintic_ui import FastSemanticUI

router = APIRouter(dependencies=[Depends(get_current_active_user)])


@router.get("/", response_model=FastSemanticUI, response_model_exclude_none=True)
@router.get("/{menu}", response_model=FastSemanticUI, response_model_exclude_none=True)
async def main_page(
        user: Annotated[User, Depends(get_current_active_user)],
        menu: str = None
) -> Union[Any]:
    """Стартовая страница"""
    return [SystemData(), UserData(user), Window()]
