from aiogram import Bot, Dispatcher
from src.bot.handlers import setup_handlers
from src.bot.middleware import setup_middlewares
from src.config.app_config import settings

bot = Bot(token=settings.token.get_secret_value())
dp = Dispatcher()


def setup_bot(app):
    setup_handlers(dp)
    setup_middlewares(dp)

    app.on_event("startup")(set_webhook)
    app.on_event("shutdown")(bot.session.close)


async def set_webhook():
    await bot.set_webhook(
        url=f"{settings.webapp_url}/webhook",
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True,
    )
