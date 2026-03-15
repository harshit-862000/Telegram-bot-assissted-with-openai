from dotenv import load_dotenv
import os
from aiogram import executor, Bot, Dispatcher, types
import openai
import sys

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

class Reference:
    """A class to represent a reference for the chatbot."""

    def __init__(self)->None:
        self.references = ""

reference= Reference()
model_name= "gpt-3.5-turbo"

# Initialize bot and dispatcher
bot= Bot(token= TELEGRAM_BOT_TOKEN)
dispatcher= Dispatcher(bot)

def clear_past():
    """Clears the past conversation history."""
    reference.response = ""

@dispatcher.message_handler(commands=['clear'])
async def clear_history(message: types.Message):
    """Handler for the /clear command to clear chat history."""
    clear_past()
    await message.reply("Chat history cleared. How can I assist you now?")



@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """Handler for the /start command."""
    await message.reply("Hello! I'm your chatbot!\ How can I assist you today?")
    
@dispatcher.message_handler(commands=['help'])  
async def help_command(message: types.Message):
    """Handler for the /help command."""
    help_commands = """Here are the available commands:
    /start - Start the bot and receive a welcome message.
    /clear - Clear the chat history.
    /help - Show this help message.
    I hope this helps! Feel free to ask me anything."""
    await message.reply(help_commands)
    
    
@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    
    """Handler for incoming messages to interact with the chatbot."""
    print(f">>> USER: \n \t {message.text}")
    response= openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message.text}
        ]
    )
    reference.response = response.choices[0]['message']['content']
    print(f">>> chatGPT: \n \t {reference.response}")
    await bot.send_message(chat_id= message.chat.id, text= reference.response)

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)