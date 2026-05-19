import os
from pyrogram import Client

# यहाँ से टोकन सीधे Railway के Variables से उठाएगा
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("my_bot", bot_token=BOT_TOKEN)

print("बोट लाइव हो रहा है...")
app.run()
