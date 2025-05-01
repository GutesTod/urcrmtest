from pydantic_settings import BaseSettings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from typing import AsyncGenerator

from settings.env.environs import env

# Настройки базы данных
class Config(BaseSettings):
    DB_USERNAME: str = env.str("DB_USERNAME", "postgres")
    DB_PASSWORD: str = env.str("DB_PASSWORD", "postgres")
    DB_HOST: str = env.str("DB_HOST", "localhost")
    DB_PORT: int = env.int("DB_PORT", 5432)
    DB_NAME: str = env.str("DB_NAME", "urcrm")

    @property
    def DB_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_USERNAME}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )