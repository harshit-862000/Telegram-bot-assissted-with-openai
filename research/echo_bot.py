import logging
from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_BOT_TOKEN= os.getenv("TELEGRAM_BOT_TOKEN")
print(TELEGRAM_BOT_TOKEN)

#configure logging
logging.basicConfig(level=logging.INFO)

#initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message: types.Message):
    
    # This handler will be called when the user sends the /start or /help command
    await message.reply("Hello! I'm an echo bot. Send me any message and I'll echo it back to you.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) 