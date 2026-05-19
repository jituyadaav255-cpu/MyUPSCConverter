from pyrogram import Client
from vars import BOT_TOKEN

# "bot_session" नाम का एक नया सेशन बनाएं
app = Client("bot_session", bot_token=BOT_TOKEN)

print("बोट लाइव है!")
app.run()
