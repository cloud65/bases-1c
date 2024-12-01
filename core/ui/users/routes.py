"""
Управление пользователями
"""
from typing import Union, Any, Annotated

from fastapi import APIRouter, Depends

from core.ui.auth.core import get_current_active_user
from core.ui.auth.models import User
from core.ui.menu.elements import Window, UserData, SystemData
from fast_semaintic_ui import FastSemanticUI, Div

router = APIRouter(dependencies=[Depends(get_current_active_user)])


#@router.get("/{users}", response_model=FastSemanticUI, response_model_exclude_none=True)
async def get_users(users: str) -> Union[Any]:
    """Стартовая страница"""
    return Div(text=users)
