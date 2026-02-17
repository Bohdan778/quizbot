# QuizBot 🤖

Telegram quiz bot built with Django.

## Features
- Random quiz questions
- Fake answers generation
- Redis cache to avoid repeated questions
- APScheduler for periodic quiz sending
- Docker & docker-compose support

## Tech Stack
- Python 3.11
- Django
- python-telegram-bot
- Redis
- Docker & Docker Compose

## Run with Docker

docker compose up --build
docker compose up

## Notes
- SQLite is used for demo purposes.
- Redis is required for caching and preventing question repeats.

