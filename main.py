import asyncio
import nest_asyncio
nest_asyncio.apply()

from pyrogram import Client
from vars import API_ID, API_HASH, BOT_TOKEN

# यह बोट को एक 'Task' के अंदर चलाएगा ताकि timeout का error न आए
async def start_bot():
    app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
    await app.start()
    print("बोट सफलता के साथ लाइव हो गया है!")
    # कनेक्शन को खुला रखने के लिए
    await asyncio.Event().wait()

if __name__ == "__main__":
    # asyncio के नए वर्ज़न के लिए यह सबसे सही तरीका है
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        pass
