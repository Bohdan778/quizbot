import os
from telegram import Bot

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = Bot(token=TOKEN)


async def send_quiz_async(question, options, correct_index):
    await bot.send_poll(
        chat_id=CHAT_ID,
        question=question,
        options=options,
        type="quiz",
        correct_option_id=correct_index,
        is_anonymous=False,
    )
