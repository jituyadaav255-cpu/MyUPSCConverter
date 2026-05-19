import asyncio
import nest_asyncio
import sys

# Event loop को फिक्स करने का सबसे पावरफुल तरीका
if sys.version_info >= (3, 8):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy() if sys.platform == 'win32' else asyncio.DefaultEventLoopPolicy())

nest_asyncio.apply()

from pyrogram import Client
from vars import API_ID, API_HASH, BOT_TOKEN

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def main():
    await app.start()
    print("बोट सफलता के साथ लाइव हो गया है!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
