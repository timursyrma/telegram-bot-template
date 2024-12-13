from aiogram import Bot, Dispatcher
from handlers import register_handlers
from src.bot.middleware import setup_middlewares
from src.config.app_config import settings

bot = Bot(token=settings.token.get_secret_value())
dp = Dispatcher()

bot.set_webhook(
    url=f"{settings.webapp_url}/webhook",
    allowed_updates=dp.resolve_used_update_types(),
    drop_pending_updates=True,
)

register_handlers(dp)
setup_middlewares(dp)
