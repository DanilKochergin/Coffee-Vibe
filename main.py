"""
Главный модуль приложения FastAPI.
Содержит роуты веб-API, раздачу статики и запуск сервера.
"""

from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from contextlib import asynccontextmanager
from typing import Optional
import os

from database import init_db, get_session, QuestSession, async_session_factory
from generator import generate_vibe_result
from config import QUESTIONS_COUNT, SOCIAL_LINK


# Модель данных для блока (настроение/стиль/состояние)
class DetailBlock(BaseModel):
    """Модель блока с детализированным описанием."""
    icon: str
    name: str
    sub: str
    emoji: str


# Модель входящих данных (баллы от фронтенда)
class ScoreRequest(BaseModel):
    """Модель запроса на генерацию результата."""
    score: int = Field(..., ge=0, le=8, description="Общий балл за ответы (0-8)")


# Модель ответа с результатом
class QuestResult(BaseModel):
    """Модель ответа с результатом квеста."""
    title: str
    description: str
    image_url: str
    emoji: str
    bg_class: str
    card_bg: str
    accent: str
    promo_code: str
    coffee_shop_name: str
    mood: DetailBlock
    style: DetailBlock
    state: DetailBlock


# Контекстный менеджер для инициализации при запуске
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Инициализация БД при старте приложения."""
    await init_db()
    yield


# Создаем приложение FastAPI
app = FastAPI(
    title="Кофейный Квест",
    description="Мобильный мини-сайт квеста для кофейни",
    version="1.0.0",
    lifespan=lifespan
)


# Подключаем раздачу статических файлов (CSS, JS, изображения)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=FileResponse)
async def root():
    """Корневой маршрут - отдает главную страницу index.html."""
    return FileResponse("index.html")


@app.post("/api/generate-vibe", response_model=QuestResult)
async def generate_vibe(
    request: ScoreRequest,
    db: AsyncSession = Depends(get_session)
):
    """
    Эндпоинт генерации результата квеста.
    Принимает баллы, сохраняет сессию в БД, возвращает результат.
    """
    result = generate_vibe_result(request.score)

    new_session = QuestSession(
        promo_code=result["promo_code"],
        score=result["score"],
        vibe_title=result["title"],
        vibe_group=result["vibe_group"],
        coffee_name=result["coffee_name"]
    )

    db.add(new_session)
    await db.commit()
    await db.refresh(new_session)

    return QuestResult(
        title=result["title"],
        description=result["description"],
        image_url=result["image_url"],
        emoji=result["emoji"],
        bg_class=result["bg_class"],
        card_bg=result["card_bg"],
        accent=result["accent"],
        promo_code=result["promo_code"],
        coffee_shop_name=result["coffee_shop_name"],
        mood=result["mood"],
        style=result["style"],
        state=result["state"]
    )


@app.get("/api/social-link")
async def get_social_link():
    """Возвращает ссылку на соцсеть кофейни для кнопки подписки."""
    return {"url": SOCIAL_LINK}


# Точка входа для запуска сервера
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
