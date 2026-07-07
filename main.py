from telegram import Bot
import os
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

async def main():
    bot = Bot(BOT_TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text="🔥 Your Motivation Bot is now connected successfully!"
    )

asyncio.run(main())