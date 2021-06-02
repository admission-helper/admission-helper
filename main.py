from vkbottle.bot import Bot
import asyncio
import asyncpg
from config import TOKEN

bot = Bot(TOKEN)

@bot.on.message()
async def handler(_) -> str:
    conn = await asyncpg.connect(user='postgres', password='postgres',
                                 database='admission', host='127.0.0.1')
    values = await conn.fetch(
        'SELECT * FROM users'
    )
    await conn.close()
    return "Асинхронный привет"

bot.run_forever()