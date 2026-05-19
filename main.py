from pyrogram import Client
from vars import BOT_TOKEN

# बस BOT_TOKEN का इस्तेमाल करें, ID और HASH की जरूरत नहीं है
app = Client("my_bot", bot_token=BOT_TOKEN)
