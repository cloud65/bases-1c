"""
Routes
"""
from fastapi import APIRouter
from core.bases.routes import router as bases_router
from core.ui.routes import router as ui_router

router = APIRouter()

router.include_router(bases_router)
router.include_router(ui_router)
