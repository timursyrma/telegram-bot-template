import asyncio
from src.bot.main import start_bot
from src.backend.main import start_backend


async def main():
    bot_task = asyncio.create_task(start_bot())
    backend_task = asyncio.create_task(start_backend())
    await asyncio.gather(bot_task, backend_task)


if __name__ == "__main__":
    asyncio.run(main())
