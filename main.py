import asyncio
import nest_asyncio
from pyrogram import Client
from modules.vars import API_ID, API_HASH, BOT_TOKEN

# यह लाइन एरर को फिक्स करेगी
nest_asyncio.apply()

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def main():
    await app.start()
    print("बोट सफलता के साथ लाइव हो गया है!")
    # बोट को चालू रखने के लिए
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
