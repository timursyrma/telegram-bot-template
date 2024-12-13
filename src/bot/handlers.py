from aiogram import F, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from src.services.search_services import search_product


async def start(message: Message):
    await message.answer("Привет!")


async def search_command(message: Message):
    if not message.photo:
        await message.answer("Пожалуйста, отправьте фото товара для поиска.")
        return

    photo = message.photo[-1]
    file_path = f"{photo.file_id}.jpg"
    await message.bot.download(file=photo.file_id, destination=file_path)

    try:
        top_10 = search_product(file_path)
        await message.answer(f"Топ-10 найденных артикулов:\n{', '.join(map(str, top_10))}")
    except Exception as e:
        await message.answer(f"Ошибка: {str(e)}")
    finally:
        # Delete local file
        import os
        if os.path.exists(file_path):
            os.remove(file_path)


def setup_handlers(dp: Dispatcher):
    dp.message.register(start, CommandStart())
    dp.message.register(search_command, F.photo)

