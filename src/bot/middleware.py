from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import Message
from typing import Callable, Awaitable, Any

from src.backend.models import User


class UserMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ) -> Any:
        if not event.from_user.username:
            return await event.answer("Set your username to use this bot.")

        data["user"], _ = await User.get_or_create(
            id=event.from_user.id, username=event.from_user.username
        )
        return await handler(event, data)


def setup_middlewares(dp: Dispatcher):
    dp.message.middleware(UserMiddleware())
