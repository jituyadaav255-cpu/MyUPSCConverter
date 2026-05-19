from pyrogram import Client
from vars import BOT_TOKEN

# "my_bot_final" नाम का बिल्कुल नया सेशन बनाएगा
app = Client("my_bot_final", bot_token=BOT_TOKEN)

print("बोट शुरू हो रहा है...")
app.run()
