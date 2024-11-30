"""
Settings
"""
import logging

from pydantic_settings import BaseSettings, SettingsConfigDict


class Database(BaseSettings):
    """
    Настройки БД
    """
    model_config = SettingsConfigDict(env_prefix='PG')
    host: str = 'localhost'
    port: int = '5432'
    user: str = 'postgres'
    password: str = ''
    database: str = 'db'


class Setting(BaseSettings):
    """
    Настройки
    """
    db: Database = Database()
    static: str = './core/static'
    log: str = 'info'
    prefix: str = '/bases'


setting = Setting()

logger = logging.getLogger('uvicorn.error')
