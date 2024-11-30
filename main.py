"""
Стартовый модуль
"""

from fastapi import FastAPI
from core.routes import router as core_router


app = FastAPI()
app.include_router(core_router)

if __name__ == '__main__':
    ...
