"""
Routes
"""

from fastapi import APIRouter
from core.ui.auth.routes import router as auth_router

router = APIRouter(prefix='/api')

router.include_router(auth_router)
