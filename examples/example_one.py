
from rubigram import Client, filters
from rubigram.types import Message


app = Client("my_account")

@app.on_message(filters.command("start", "/"))
async def handler(message):
    await message.reply("Hello, World!")

app.run()
