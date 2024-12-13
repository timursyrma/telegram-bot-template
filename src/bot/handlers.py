from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message


async def start(message: Message):
    await message.answer("Hello World!")


def register_handlers(dp: Dispatcher):
    dp.message.register(start, CommandStart())
