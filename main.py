import asyncio
import nest_asyncio
nest_asyncio.apply()

from pyrogram import Client
# यहाँ से modules. हटा दिया है, क्योंकि vars.py सीधे रूट फोल्डर में है
from vars import API_ID, API_HASH, BOT_TOKEN

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def main():
    await app.start()
    print("बोट सफलता के साथ लाइव हो गया है!")
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
