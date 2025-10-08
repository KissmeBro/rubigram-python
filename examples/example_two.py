
from rubigram.bot import BotClient, filters

app = BotClient("BOT-TOKEN")

@app.on_message(filters.private)
async def handler(client, message):
    await message.reply("Hello, World!")

app.run()
