"""
Модуль работы с базой данных.
SQLAlchemy модели и асинхронный сетап для SQLite через aiosqlite.
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime
from datetime import datetime

from config import DATABASE_NAME


# Базовый класс для всех моделей
class Base(DeclarativeBase):
    pass


# Модель сессии квеста (хранит результат прохождения теста)
class QuestSession(Base):
    __tablename__ = "quest_sessions"

    # Уникальный идентификатор записи
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    # Уникальный промокод формата COFFEE-XXXX
    promo_code: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    # Набранные баллы (от 0 до 8)
    score: Mapped[int] = mapped_column(Integer)
    # Сгенерированное название вайба
    vibe_title: Mapped[str] = mapped_column(String(100))
    # Группа настроения (dark/neutral/bright)
    vibe_group: Mapped[str] = mapped_column(String(20))
    # Выбранный кофе
    coffee_name: Mapped[str] = mapped_column(String(50))
    # Время создания записи
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


# Создаем асинхронный движок для SQLite
DATABASE_URL = f"sqlite+aiosqlite:///{DATABASE_NAME}"

engine = create_async_engine(
    DATABASE_URL,
    echo=False  # Отключаем логирование SQL-запросов для продакшена
)

# Фабрика асинхронных сессий
async_session_factory = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def init_db():
    """Инициализация базы данных: создание таблиц если их нет."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    """Контекстный менеджер для получения сессии БД."""
    async with async_session_factory() as session:
        yield session
