import os
import asyncio
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from openai import AsyncOpenAI

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = Bot(token=BOT_TOKEN)
client = AsyncOpenAI(api_key=OPENAI_API_KEY)

async def generate_message():
    response = await client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a world-class motivational speaker."
            },
            {
                "role": "user",
                "content": (
                    "Write one unique motivational message under 120 words. "
                    "Make it powerful, inspiring, and end with 2 relevant emojis."
                )
            }
        ]
    )
    return response.choices[0].message.content

async def send_message():
    text = await generate_message()
    await bot.send_message(
        chat_id=CHAT_ID,
        text=text
    )

async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_message, "interval", hours=1)
    scheduler.start()

    await send_message()

    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())