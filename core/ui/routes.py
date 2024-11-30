"""
Routes
"""

from fastapi import APIRouter, Depends

from core.ui.auth.core import get_current_active_user
from core.ui.auth.routes import router as auth_router
from core.ui.menu import router as menu_router

router = APIRouter(prefix='/api')

router.include_router(auth_router)

router.include_router(menu_router, dependencies=[Depends(get_current_active_user)])
