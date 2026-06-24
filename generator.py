"""
Модуль процедурной генерации результатов квеста.
Чистая функция, которая на основе балла генерирует уникальный результат.
"""

import random
import hashlib
from datetime import datetime

from config import (
    VIBE_DATA, VIBE_RANGES, COFFEE_MENU, DESCRIPTIONS,
    MOODS, STYLES, STATES, COFFEE_SHOP_NAME
)


def get_vibe_group(score: int) -> str:
    """
    Определяет группу настроения по количеству баллов.
    Возвращает ключ группы: 'dark', 'neutral' или 'bright'.
    """
    for group_key, (min_score, max_score) in VIBE_RANGES.items():
        if min_score <= score <= max_score:
            return group_key
    return "neutral"


def generate_promo_code(score: int) -> str:
    """
    Генерирует уникальный промокод формата COFFEE-XXXX.
    """
    unique_string = f"{datetime.utcnow().isoformat()}-{score}-{random.randint(1000, 9999)}"
    hash_hex = hashlib.md5(unique_string.encode()).hexdigest()[:4].upper()
    return f"COFFEE-{hash_hex}"


def generate_vibe_result(score: int) -> dict:
    """
    Главная функция генерации результата.
    Принимает общий балл (0-8), возвращает словарь с детализированным результатом.
    """
    score = max(0, min(8, score))

    vibe_group = get_vibe_group(score)
    vibe_data = VIBE_DATA[vibe_group]

    vibe_name = random.choice(vibe_data["names"])
    coffee_name = random.choice(list(COFFEE_MENU.keys()))
    coffee_image = COFFEE_MENU[coffee_name]

    if vibe_name.endswith("-"):
        full_title = f"{vibe_name}{coffee_name}"
    else:
        full_title = f"{vibe_name} {coffee_name}"

    description_text = random.choice(DESCRIPTIONS)

    mood = random.choice(MOODS)
    style = random.choice(STYLES)
    state = random.choice(STATES)

    promo_code = generate_promo_code(score)
    image_url = f"/static/images/{coffee_image}"

    return {
        "title": full_title,
        "description": description_text,
        "image_url": image_url,
        "emoji": vibe_data["emoji"],
        "bg_class": vibe_data["bg_class"],
        "card_bg": vibe_data["card_bg"],
        "accent": vibe_data["accent"],
        "promo_code": promo_code,
        "vibe_group": vibe_group,
        "coffee_name": coffee_name,
        "score": score,
        "coffee_shop_name": COFFEE_SHOP_NAME,
        "mood": {
            "icon": mood["icon"],
            "name": mood["name"],
            "sub": mood["sub"],
            "emoji": mood["emoji"]
        },
        "style": {
            "icon": style["icon"],
            "name": style["name"],
            "sub": style["sub"],
            "emoji": style["emoji"]
        },
        "state": {
            "icon": state["icon"],
            "name": state["name"],
            "sub": state["sub"],
            "emoji": state["emoji"]
        }
    }
