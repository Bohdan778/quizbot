import random
import asyncio
import threading

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from django.core.cache import cache
from asgiref.sync import sync_to_async

from phrases.models import Phrase
from bot.telegram_bot import send_quiz_async


CACHE_TTL = 60 * 60 * 24 * 7 

scheduler = AsyncIOScheduler()
scheduler_started = False


@sync_to_async
def get_available_phrase():
    phrases = Phrase.objects.filter(is_fake=False)
    if not phrases.exists():
        return None

    available = [
        p for p in phrases
        if not cache.get(f"phrase_sent_{p.id}")
    ]

    if not available:
        return None

    return random.choice(available)


@sync_to_async
def get_fake_answers(correct_text):
    return list(
        Phrase.objects
        .filter(is_fake=True)
        .exclude(text=correct_text)
        .order_by("?")[:2]
    )


@sync_to_async
def mark_phrase_used(phrase_id):
    cache.set(f"phrase_sent_{phrase_id}", True, CACHE_TTL)


async def job():
    phrase = await get_available_phrase()
    if not phrase:
        return

    correct_answer = phrase.translation
    if not correct_answer:
        return

    fake_answers = await get_fake_answers(correct_answer)
    if len(fake_answers) < 2:
        return

    options = [
        correct_answer,
        fake_answers[0].text,
        fake_answers[1].text,
    ]
    random.shuffle(options)

    correct_index = options.index(correct_answer)

    await send_quiz_async(
        question=phrase.text,
        options=options,
        correct_index=correct_index
    )

    await mark_phrase_used(phrase.id)


async def _start():
    scheduler.add_job(job, "interval", seconds=10)
    scheduler.start()

    while True:
        await asyncio.sleep(3600)


def start_scheduler():
    global scheduler_started

    if scheduler_started:
        return

    scheduler_started = True

    def runner():
        asyncio.run(_start())

    thread = threading.Thread(target=runner, daemon=True)
    thread.start()
