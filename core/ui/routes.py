"""
Routes
"""

from fastapi import APIRouter
from fastapi.responses import FileResponse

from core.ui.auth.routes import router as auth_router
from core.ui.menu.routes import router as menu_router
from core.ui.users.routes import router as users_router

router = APIRouter(prefix='/api')


@router.get("/static/{path:path}")
async def get_static(path: str):
    """Получение изображений"""
    return FileResponse(f'core/static/{path}')


router.include_router(auth_router)

router.include_router(menu_router)

router.include_router(users_router, prefix='/content')
