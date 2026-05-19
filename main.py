from pyrogram import Client, idle
from vars import BOT_TOKEN

# Client सेटअप
app = Client("my_bot", bot_token=BOT_TOKEN)

async def main():
    await app.start()
    print("बोट सफलता के साथ लाइव हो गया है!")
    # यह बोट को टेलीग्राम पर एक्टिव रखता है ताकि वो मैसेजेस सुन सके
    await idle() 

if __name__ == "__main__":
    app.run(main())
