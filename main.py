# pylint: disable=missing-function-docstring, unused-argument, redefined-outer-name
"""
Стартовый модуль
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.bases.stotage.db import StorageDatabase
from core.bases.stotage.models import bind_models
from core.config import setting
from core.routes import router as core_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = StorageDatabase(setting=setting.db)
    bind_models(db)
    yield
    db.close()


app = FastAPI(lifespan=lifespan)
app.include_router(core_router)

if __name__ == '__main__':
    ...
