from pyrogram import Client
from vars import BOT_TOKEN

# API_ID और HASH को None रखें ताकि सिर्फ टोकन का उपयोग हो
app = Client(
    "my_bot",
    api_id=None,
    api_hash=None,
    bot_token=BOT_TOKEN
)

print("बोट शुरू हो रहा है...")
app.run()
