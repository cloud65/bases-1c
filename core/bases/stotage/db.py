# pylint: disable=missing-function-docstring, unused-argument, missing-class-docstring,
# pylint: disable=logging-fstring-interpolation
"""
Базы данных
"""
import psycopg2
from peewee import PostgresqlDatabase
from pydantic_settings import BaseSettings

from core.config import logger


class StorageDatabase(PostgresqlDatabase):
    def __init__(self, setting: BaseSettings):
        self.create_database(setting)
        super().__init__(
            database=setting.name,
            host=setting.host,
            port=setting.port,
            user=setting.user,
            password=setting.password,
        )

    @classmethod
    def create_database(cls, setting: BaseSettings):
        conn = psycopg2.connect(
            host=setting.host,
            port=setting.port,
            user=setting.user,
            password=setting.password,
        )
        cur = conn.cursor()
        conn.autocommit = True

        query = f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{setting.name}'"
        cur.execute(query)
        exists = cur.fetchone()

        if exists is None:
            query = f'CREATE DATABASE "{setting.name}"'
            cur.execute(query)
            logger.warning(f'База данных создана - {setting.name}')
        else:
            logger.info(f'База данных существует - {setting.name}')

        conn.close()
