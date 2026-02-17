import asyncio
import os
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = Bot(token=TOKEN)

async def main():
    await bot.send_poll(
        chat_id=CHAT_ID,
        question="Що таке Django?",
        options=[
            "Web framework",
            "База даних",
            "Операційна система"
        ],
        type="quiz",
        correct_option_id=0
    )


asyncio.run(main())
