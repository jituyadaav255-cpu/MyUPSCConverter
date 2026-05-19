from pyrogram import Client
from vars import BOT_TOKEN

# ":memory:" का मतलब है कि कोई भी पुरानी .session फाइल इस्तेमाल नहीं होगी
app = Client(":memory:", bot_token=BOT_TOKEN)

print("बोट लाइव है!")
app.run()
