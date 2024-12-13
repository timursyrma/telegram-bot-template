from fastapi import APIRouter, FastAPI, Request
from src.bot.main import bot, dp
from aiogram.types import Update

router = APIRouter()


@router.post("/webhook")
async def webhook(request: Request):
    update = Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)


@router.get("/health-check")
async def health_check():
    return {"status": "ok"}


def setup_routers(app: FastAPI):
    app.include_router(router)
