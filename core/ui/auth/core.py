# pylint: disable=missing-function-docstring
"""
Функции авторизации
"""
from datetime import timezone, datetime, timedelta
from typing import Annotated, Union

import jwt

from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError

from core.bases.stotage.models import Users
from core.config import setting
from core.ui.auth.models import TokenData, User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")

credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )


def verify_password(plain_password, db_password):
    return Users.hash_md5(plain_password) == db_password.tobytes()




def get_user(username: str) -> Union[Users, None]:
    return Users.get_or_none(name=username)


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, setting.auth.secret_key, algorithm=setting.auth.algorithm)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, setting.auth.secret_key, algorithms=[setting.auth.algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError as exc:
        raise credentials_exception from exc
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return User.from_orm(user)


async def get_current_active_user(
        current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
