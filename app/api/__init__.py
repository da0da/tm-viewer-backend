from fastapi import FastAPI

from app.api.gbx.handlers import router as gbx_router


def init_routers(app: FastAPI) -> None:
    app.include_router(gbx_router, prefix="/api", tags=["gbx"])
