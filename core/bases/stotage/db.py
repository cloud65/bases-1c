# pylint: disable=missing-function-docstring, unused-argument, missing-class-docstring,
# pylint: disable=logging-fstring-interpolation,protected-access
"""
Базы данных
"""
import psycopg2
from peewee import PostgresqlDatabase
from playhouse.migrate import PostgresqlMigrator, migrate
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

    @staticmethod
    def migrate(db, model):
        """Процедуры миграции"""
        table_name = model._meta.table_name

        if not db.table_exists(table_name):
            model.create_table()
            return {table_name: 'create'}

        migrator = PostgresqlMigrator(db)
        list_migrate, info = [], []

        # Колонки
        model_fields = model._meta.columns
        db_columns = db.get_columns(table_name)

        set_db = set(i.name for i in db_columns)
        set_model = set(model_fields.keys())

        for name in (set_db - set_model):
            list_migrate.append(migrator.drop_column(table_name, name))
            info.append({name: 'drop'})

        for name in (set_model - set_db):
            list_migrate.append(
                migrator.add_column(table_name, name, model_fields[name])
            )
            info.append({name: 'add'})

        # Индексы
        db_indexes = db.get_indexes(table_name)
        model_indexes = {idx._name: idx for idx in model._meta.indexes}
        db_names = [idx.name for idx in db_indexes]

        add = set(model_indexes.keys()) - set(db_names)
        for name in add:
            migrator.add_index(
                table_name,
                model_indexes[name]._expressions,
                model_indexes[name]._unique
            )
            info.append({f"index: {name}": 'add'})

        if len(list_migrate) > 0:
            migrate(*list_migrate)
        return {table_name: info}
