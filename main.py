# main.py
import asyncio
from pyrogram import Client, filters
from modules.vars import API_ID, API_HASH, BOT_TOKEN

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("नमस्ते! मैं UPSC कनवर्टर बोट हूँ। अपनी फाइल भेजें!")

print("बोट शुरू हो गया है...")
app.run()
