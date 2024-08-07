from fastapi import FastAPI, HTTPException
from starlette.responses import RedirectResponse
from contextlib import asynccontextmanager
import uvicorn

from api import router as api_router
from pages.router import router as pages_router
from core.config import settings
from core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    db_helper.dispose()

main_app = FastAPI(
    lifespan=lifespan
)

main_app.include_router(
    api_router,
    prefix=settings.api.prefix
)

main_app.include_router(
    pages_router,
    prefix=settings.api.prefix
)

@main_app.get("/")
async def root_redirect():
    return RedirectResponse(url="/api/pages/admin")

if __name__ == "__main__":
    uvicorn.run(app="main:main_app",
                host=settings.run.host,
                port=settings.run.port,
                reload=True)
