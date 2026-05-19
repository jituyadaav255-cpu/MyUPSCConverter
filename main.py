from pyrogram import Client
from vars import BOT_TOKEN

# क्लाइंट को इनिशियलाइज़ करें
app = Client("my_bot", bot_token=BOT_TOKEN)

# यह Pyrogram का अपना तरीका है बोट को चलाने का
print("बोट लाइव हो रहा है...")
app.run()
