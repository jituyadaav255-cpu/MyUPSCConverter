import asyncio
from pyrogram import Client
from modules.vars import API_ID, API_HASH, BOT_TOKEN

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def main():
    await app.start()
    print("बोट सफलता के साथ लाइव हो गया है!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
