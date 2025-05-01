from settings.database.config import Config
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from typing import AsyncGenerator

class Database:
    def __init__(self):
        # Инициализация настроек
        self.settings = Config()
        # Создание асинхронного движка
        self.engine = create_async_engine(self.settings.DB_URL, echo=True, future=True)
        # Создание фабрики сессий
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session
            await session.close()