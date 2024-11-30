# pylint: disable=missing-function-docstring
"""
Routes
"""
from datetime import timedelta


from fastapi import APIRouter

from core.config import setting
from core.ui.auth.core import create_access_token, authenticate_user
from core.ui.auth.form import page_login
from core.ui.auth.models import AuthData
from fast_semaintic_ui import FastSemanticUI, EventAuth
from fast_semaintic_ui.auth import AuthError
from fast_semaintic_ui.types import AnyElement

router = APIRouter(prefix='/auth')


@router.post("/token", response_model=FastSemanticUI, response_model_exclude_none=True)
async def login_for_access_token(auth_data: AuthData) -> EventAuth:
    user = authenticate_user(auth_data.username, auth_data.password)
    if not user:
        raise AuthError(message='Неверный логин или пароль', code='auth')
    access_token_expires = timedelta(minutes=setting.auth.token_expire)
    access_token = create_access_token(
        data={"sub": user.name}, expires_delta=access_token_expires
    )
    return EventAuth(url='/', token=access_token)


@router.get("/login", response_model=FastSemanticUI, response_model_exclude_none=True)
async def get_page_login() -> list[AnyElement]:
    return page_login()