import asyncio
# सबसे पहले nest_asyncio अप्लाई करें
import nest_asyncio
nest_asyncio.apply()

# अब Pyrogram को इंपोर्ट करें
from pyrogram import Client
from modules.vars import API_ID, API_HASH, BOT_TOKEN

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def main():
    await app.start()
    print("बोट सफलता के साथ लाइव हो गया है!")
    # बोट को चालू रखने के लिए
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
