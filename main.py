import os
from pyrogram import Client

# यहाँ हम सीधे Railway की सेटिंग से TOKEN उठा रहे हैं
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Client सेटअप
app = Client("my_bot", bot_token=BOT_TOKEN)

print("बोट लाइव हो रहा है...")
app.run()
