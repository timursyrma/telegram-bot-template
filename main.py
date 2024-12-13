import uvicorn
from src.backend.main import create_app
from src.bot.main import setup_bot
from src.config.app_config import settings


app = create_app()
setup_bot(app)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.app_host, port=settings.app_port)