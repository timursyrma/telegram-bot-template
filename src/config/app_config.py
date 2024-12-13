from pydantic import SecretStr
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    token: SecretStr
    db_url: SecretStr
    webapp_url: str
    app_host: str
    app_port: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = AppConfig()
