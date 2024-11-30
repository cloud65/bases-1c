"""
Settings
"""
import logging

from pydantic_settings import BaseSettings, SettingsConfigDict


class Database(BaseSettings):
    """
    Настройки БД
    """
    model_config = SettingsConfigDict(env_prefix='PG_')
    host: str = 'localhost'
    port: int = '5432'
    user: str = 'postgres'
    password: str = ''
    name: str = 'db'


class AuthSettings(BaseSettings):
    """
    Параметры авторизации
    """
    secret_key: str = "09d25e012faa6ca2556c818166b7a9563b93f7099f677f4caa6cf63b88e8d3e7"
    algorithm: str = "HS256"
    token_expire: int = 30


class Setting(BaseSettings):
    """
    Настройки
    """
    db: Database = Database()
    auth: AuthSettings = AuthSettings()
    static: str = './core/static'
    log: str = 'info'
    prefix: str = '/bases'


setting = Setting()

logger = logging.getLogger('uvicorn.error')
