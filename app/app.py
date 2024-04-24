from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api import init_routers
from app.dependencies.webapp import WebAppContainer


def create_app() -> FastAPI:
    WebAppContainer()

    app = FastAPI()

    origins = [
        "*",
    ]

    app.add_middleware(
        CORSMiddleware,  # type: ignore[call-arg]
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    init_routers(app)

    return app
