from fastapi import FastAPI

from app.api import init_routers
from app.dependencies.webapp import WebAppContainer


def create_app() -> FastAPI:
    WebAppContainer()
    app = FastAPI()
    init_routers(app)

    return app
