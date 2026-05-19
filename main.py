import sys
import asyncio

# यह जुगाड़ 3.14 के सख्त timeout नियमों को बाईपास करेगा
if sys.version_info >= (3, 11):
    def run_wrapper(coro):
        return asyncio.run(coro)
else:
    def run_wrapper(coro):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(coro)

# अब Pyrogram को इम्पोर्ट करें
from pyrogram import Client
from vars import API_ID, API_HASH, BOT_TOKEN

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def start_bot():
    await app.start()
    print("बोट लाइव है!")
    await asyncio.Future()

if __name__ == "__main__":
    try:
        run_wrapper(start_bot())
    except Exception as e:
        print(f"एरर: {e}")
