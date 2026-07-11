# ☕ Coffee Vibe Quest

> Interactive mobile-first quiz that matches your mood to a perfect coffee drink — built with FastAPI, async SQLAlchemy, and procedural generation.

---

## 🎯 About The Project

**Coffee Vibe Quest** is a gamified single-page application designed for specialty coffee shops. Users answer 4 playful personality questions, and the system generates a personalized "coffee vibe" result — matching their mood to a specific drink with a unique promo code.

The project was initially commissioned as a marketing tool for a local coffee shop, but its clean architecture and polished UI made it a strong portfolio piece. The entire result generation is **procedural** — no AI, no external APIs — just pure logic and randomness for instant, fun results.

### How It Works

1. User lands on a minimal welcome screen with animated SVG illustration
2. Answers 4 curated questions (battery level, headspace, music vibe, evening plans)
3. Backend calculates a score (0–8), selects a mood group, coffee type, and generates a unique `COFFEE-XXXX` promo code
4. Result screen displays a cinematic card with the drink photo, emoji badge, and 3 personality breakdowns (Mood / Style / State)
5. User clicks CTA → opens social link → sees their promo code

---

## ✨ Key Features

- 🎨 **Scandinavian Minimal UI** — warm concrete palette, glassmorphism cards, smooth fade/slide animations
- 📱 **Mobile-First SPA** — fully responsive, touch-optimized, no framework overhead
- ☕ **Procedural Generation** — instant unique results from 10 coffee types × 30 mood adjectives × 12 mood/style/state descriptors
- 🔐 **Unique Promo Codes** — `COFFEE-XXXX` format, MD5-hashed for uniqueness, stored in SQLite
- ⚡ **Async Backend** — FastAPI + aiosqlite for non-blocking database operations
- 🎭 **Animated SVG Illustrations** — hand-drawn coffee cup with floating steam, no image dependencies on landing
- 🌗 **Dynamic Theming** — result screen background adapts to mood group (dark/neutral/bright)
- 🏗️ **Amvera Cloud Ready** — `amvera.yml` included for one-click deployment

---

## 🛠 Tech Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| **Backend** | Python 3.11 + FastAPI | High-performance async framework, automatic OpenAPI docs |
| **Database** | SQLite + SQLAlchemy (async) + aiosqlite | Zero-config DB, perfect for single-server deployment |
| **Frontend** | HTML5 + Tailwind CSS (CDN) + Vanilla JS | No build step, instant load, mobile-first utility classes |
| **Animations** | CSS Keyframes + Intersection-free JS | Smooth 60fps transitions without heavy animation libraries |
| **Deployment** | Amvera Cloud (container) | One-click deploy with `amvera.yml` |
| **Typography** | Inter (Google Fonts) | Clean, modern, excellent readability on mobile |

---

## 📁 Project Structure

```
coffee-vibe-quest/
├── config.py            # App settings, quiz data, coffee menu, mood arrays
├── database.py          # SQLAlchemy models, async engine, session factory
├── generator.py         # Procedural result generation (score → vibe → promo)
├── main.py              # FastAPI app, routes, static file serving
├── requirements.txt     # Python dependencies
├── amvera.yml           # Amvera Cloud deployment config
├── index.html           # Single-page frontend (welcome → quiz → result)
├── static/
│   └── images/          # Coffee drink photos (10 images)
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/coffee-vibe-quest.git
cd coffee-vibe-quest

# Install dependencies
pip install -r requirements.txt

# Add coffee images to static/images/
# Required: raf.jpg, flat_white.jpg, cappuccino.jpg, filter.jpg,
#           latte.jpg, espresso_tonic.jpg, americano.jpg,
#           matcha.jpg, bumble.jpg, cold_brew.jpg

# Run the server
python main.py
```

Open **http://localhost:8000** in your browser (mobile viewport recommended).

### Quick Start (Development)

```bash
# Server runs with auto-reload on port 8000
python main.py
# → http://localhost:8000
```

---

## 🗺 Roadmap / Future Plans

- [ ] 🌙 Dark mode toggle with system preference detection
- [ ] 📊 Admin dashboard — view quest stats, promo code usage, popular drinks
- [ ] 🔗 Telegram Bot integration — send promo codes directly to users
- [ ] 🗺 Yandex Maps widget — show nearest coffee shop location
- [ ] 🌐 Multi-language support (RU / EN)
- [ ] 📸 Share result card to Instagram Stories (canvas-based image generation)
- [ ] 🎯 A/B testing for quiz questions and result formats
- [ ] 📱 PWA support — installable home screen, offline caching

---

## 📄 License

MIT License — feel free to use this project in your portfolio or for learning.

---

<p align="center">
  Made with ☕ and clean code
</p>

---

# ☕ Coffee Vibe Quest

> Интерактивный мобильный квиз, который подбирает идеальный кофейный напиток под ваше настроение — построен на FastAPI, async SQLAlchemy и процедурной генерации.

---

## 🎯 О проекте

**Coffee Vibe Quest** — геймифицированное одностраничное приложение для специализированных кофеен. Пользователь отвечает на 4 игривых вопроса о личности, а система генерирует персональный результат «кофе вайв» — подбирает напиток под настроение с уникальным промокодом.

Проект изначально задумывался как маркетинговый инструмент для локальной кофейни, но его чистая архитектура и отполированный интерфейс сделали его сильным портфолио-проектом. Вся генерация результатов **процедурная** — без AI, без внешних API — только чистая логика и случайность для мгновенных и весёлых результатов.

### Как это работает

1. Пользователь попадает на минималистичный экран приветствия с анимированной SVG-иллюстрацией
2. Отвечает на 4 подобранных вопроса (уровень заряда, настроение, музыкальный вайв, планы на вечер)
3. Бэкенд рассчитывает оценку (0–8), выбирает группу настроения, тип кофе и генерирует уникальный промокод `COFFEE-XXXX`
4. Экран результата отображает кинематографичную карточку с фото напитка, эмодзи-бейджем и 3 описаниями личности (Настроение / Стиль / Состояние)
5. Пользователь нажимает CTA → переходит по социальной ссылке → видит свой промокод

---

## ✨ Ключевые особенности

- 🎨 **Скандинавский минималистичный UI** — тёплая бетонная палитра, карточки с стеклоподобным эффектом, плавные анимации появления/скольжения
- 📱 **Mobile-First SPA** — полностью адаптивный, оптимизированный под тач, без накладных расходов фреймворков
- ☕ **Процедурная генерация** — мгновенные уникальные результаты из 10 типов кофе × 30 прилагательных настроения × 12 описаний настроения/стиля/состояния
- 🔐 **Уникальные промокоды** — формат `COFFEE-XXXX`, MD5-хеши для уникальности, хранение в SQLite
- ⚡ **Асинхронный бэкенд** — FastAPI + aiosqlite для неблокирующих операций с базой данных
- 🎭 **Анимированные SVG-иллюстрации** — рисованная кофейная чашка с парящим паром, без зависимости от изображений на лендинге
- 🌗 **Динамическая тема** — фон экрана результата адаптируется к группе настроения (тёмная/нейтральная/яркая)
- 🏗️ **Готовность к Amvera Cloud** — `amvera.yml` включён для деплоя в один клик

---

## 🛠 Технологический стек

| Уровень | Технология | Почему |
|---------|-----------|--------|
| **Бэкенд** | Python 3.11 + FastAPI | Высокопроизводительный асинхронный фреймворк, автодокументация OpenAPI |
| **База данных** | SQLite + SQLAlchemy (async) + aiosqlite | БД без настроек, идеальна для одиночного сервера |
| **Фронтенд** | HTML5 + Tailwind CSS (CDN) + Vanilla JS | Без этапа сборки, мгновенная загрузка, mobile-first утилитарные классы |
| **Анимации** | CSS Keyframes + JS без Intersection | Плавные переходы 60fps без тяжёлых библиотек анимаций |
| **Деплой** | Amvera Cloud (контейнер) | Деплой в один клик через `amvera.yml` |
| **Типографика** | Inter (Google Fonts) | Чистая, современная, отличная читаемость на мобильных |

---

## 📁 Структура проекта

```
coffee-vibe-quest/
├── config.py            # Настройки приложения, данные квиза, меню кофе, массивы настроений
├── database.py          # Модели SQLAlchemy, async engine, фабрика сессий
├── generator.py         # Процедурная генерация результатов (оценка → вайв → промо)
├── main.py              # Приложение FastAPI, маршруты, раздача статики
├── requirements.txt     # Зависимости Python
├── amvera.yml           # Конфигурация деплоя в Amvera Cloud
├── index.html           # Одностраничный фронтенд (приветствие → квиз → результат)
├── static/
│   └── images/          # Фото кофейных напитков (10 изображений)
└── README.md
```

---

## 🚀 Быстрый старт

### Требования

- Python 3.11+
- pip

### Установка

```bash
# Клонировать репозиторий
git clone https://github.com/your-username/coffee-vibe-quest.git
cd coffee-vibe-quest

# Установить зависимости
pip install -r requirements.txt

# Добавить изображения кофе в static/images/
# Обязательные: raf.jpg, flat_white.jpg, cappuccino.jpg, filter.jpg,
#               latte.jpg, espresso_tonic.jpg, americano.jpg,
#               matcha.jpg, bumble.jpg, cold_brew.jpg

# Запустить сервер
python main.py
```

Откройте **http://localhost:8000** в браузере (рекомендуется мобильный вид).

### Быстрый старт (разработка)

```bash
# Сервер запускается с авторелоадом на порту 8000
python main.py
# → http://localhost:8000
```

---

## 🗺 Дорожная карта

- [ ] 🌙 Тёмная тема с определением системных предпочтений
- [ ] 📊 Админ-панель — статистика квиза, использование промокодов, популярные напитки
- [ ] 🔗 Интеграция с Telegram Bot — отправка промокодов пользователям
- [ ] 🗺 Виджет Яндекс Карт — показать ближайшую кофейню
- [ ] 🌐 Мультиязычность (RU / EN)
- [ ] 📸 Шаринг карточки результата в Instagram Stories (генерация изображения через canvas)
- [ ] 🎯 A/B тестирование вопросов квиза и форматов результатов
- [ ] 📱 PWA — установка на домашний экран, офлайн-кэширование

---

## 📄 Лицензия

MIT License — свободно используйте этот проект в своём портфолио или для обучения.

---

<p align="center">
  Сделано с ☕ и чистым кодом
</p>
