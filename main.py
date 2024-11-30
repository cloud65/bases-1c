# pylint: disable=missing-function-docstring, unused-argument, redefined-outer-name
"""
Стартовый модуль
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from core.bases.stotage.db import StorageDatabase
from core.bases.stotage.models import bind_models
from core.config import setting
from core.routes import router as core_router

from fast_semaintic_ui.auth import auth_exception_handling
from fast_semaintic_ui.html import get_html


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = StorageDatabase(setting=setting.db)
    bind_models(db)
    yield
    db.close()


app = FastAPI(lifespan=lifespan)
auth_exception_handling(app)

app.include_router(core_router)


@app.get('/{path:path}', tags=['Init'])
async def html_landing() -> HTMLResponse:
    """Выдача html через FastAPI. Для отладки"""
    return HTMLResponse(get_html())


if __name__ == '__main__':
    ...
