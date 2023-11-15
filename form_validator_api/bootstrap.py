from functools import lru_cache

from fastapi import APIRouter, FastAPI

from .settings import get_settings
from .routers.form_validator_router import router as form_validator_router

def _setup_api_routers(
    api: APIRouter,
) -> None:
    api.include_router(form_validator_router, tags=['form_validator_router'])


@lru_cache
def make_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.project_name,
    )
    _setup_api_routers(app.router)

    return app