import os
import random
import asyncio
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

quotes = [
    "🔥 Never give up. Every expert was once a beginner.",
    "💪 Discipline beats motivation.",
    "🚀 Success comes from consistency, not luck.",
    "🏆 Keep going. Your future self will thank you.",
    "⏳ Small progress every hour is still progress.",
    "🌟 Dreams work when you do.",
    "🔥 Winners never quit, and quitters never win.",
    "📈 Stay focused. Stay patient. Stay strong.",
    "💯 One more step today is better than none.",
    "⚡ Believe in yourself and keep moving forward."
]

async def send_quote():
    await bot.send_message(
        chat_id=CHAT_ID,
        text=random.choice(quotes)
    )

async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_quote, "interval", hours=1)
    scheduler.start()

    await send_quote()

    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())