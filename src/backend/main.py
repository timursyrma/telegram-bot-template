from fastapi import FastAPI
from src.backend.routers import setup_routers
from src.config.app_config import settings
from tortoise import Tortoise


def create_app() -> FastAPI:
    app = FastAPI(title="Telegram Bot Backend", version="1.0.0")

    setup_routers(app)

    @app.on_event("startup")
    async def startup_event():
        await Tortoise.init(
            db_url=settings.db_url.get_secret_value(),
            modules={"models": ["src.models"]}
        )
        await Tortoise.generate_schemas()

    @app.on_event("shutdown")
    async def shutdown_event():
        await Tortoise.close_connections()

    return app
