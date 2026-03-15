# Telegram Bot Assisted with OpenAI

A simple Telegram chatbot powered by OpenAI that can answer user queries directly inside Telegram.

The bot receives user messages, sends them to the OpenAI API, and returns the generated response.

---

## Features

- Telegram chatbot built using **aiogram**
- AI responses generated using **OpenAI GPT model**
- Environment variables for secure API key storage
- Basic bot commands for interaction
- Lightweight and easy to extend

---

## Project Structure

Telegram-bot-assissted-with-openai/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── LICENSE

---

## Requirements

Install the following Python packages:

- aiogram
- openai
- python-dotenv

Install dependencies using:
pip install -r requirements.txt


---

## Installation

Clone the repository:
git clone https://github.com/your-username/Telegram-bot-assissted-with-openai.git

Move into the project folder:
cd Telegram-bot-assissted-with-openai

Install dependencies:
pip install -r requirements.txt


---

## Create Telegram Bot

1. Open **Telegram**
2. Search for **BotFather**
3. Run the following commands:

/start
/newbot


4. Follow the instructions and copy the **Bot Token**

---

## Get OpenAI API Key

1. Go to:
https://platform.openai.com/api-keys

2. Create a new API key
3. Copy the key

---

## Environment Variables

Create a `.env` file in the root directory.

Example:
OPENAI_API_KEY=your_openai_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token


---

## Running the Bot

Start the bot using:
python main.py


The bot will start polling Telegram servers and respond to user messages.

---

## Available Commands

| Command | Description |
|------|-------------|
| /start | Start the bot and receive a welcome message |
| /help | Show help instructions |
| /clear | Clear the chat history |

---

## How It Works

1. User sends a message to the Telegram bot.
2. The bot receives the message using **aiogram dispatcher**.
3. The message is sent to the **OpenAI API**.
4. OpenAI generates a response.
5. The bot sends the response back to the user.

---

## Security Note

Never push your `.env` file or API keys to GitHub.

Add `.env` to `.gitignore` to keep credentials safe.

Example `.gitignore`:
.env
pycache/
*.pyc
venv/


---

## License

This project is licensed under the MIT License.
