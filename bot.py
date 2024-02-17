import os
import sys
import requests
from dotenv import load_dotenv
from main import dbcon, update_db

load_dotenv()
TOKEN = os.environ.get("BOT_TOKEN")

# Replace "YOUR_TOKEN" with your actual bot token
BOT_TOKEN = "YOUR_TOKEN"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"

# Define a function to send messages
def send_message(chat_id, text):
    url = BASE_URL + "sendMessage"
    data = {"chat_id": chat_id, "text": text}
    response = requests.post(url, json=data)
    return response.json()


# Define a function to handle commands
def handle_command(command, chat_id):
    if command == '/start':
        send_message(chat_id, "Hello! This is a simple echo bot. Send me a message, and I'll echo it back to you.")
    elif command == '/conn':
        if dbcon:
            send_message(chat_id, "Database connectivity successful.")
        else:
            send_message(chat_id, "Database didn't connect.")
    elif command.startswith('/spend'):
        # pass
        _, amount, category = command.split()
        amount = int(amount)  # Convert amount to integer
        if update_db('insert', amount, category):
            send_message(chat_id, f"Logged expenditure of {amount} rupees on {category}.")
    # elif command == '/stop':
    #     send_message(chat_id, "Bot session ended. Bye!")
    #     sys.exit()
    elif command == '/help':
        send_message(chat_id, "Available commands:\n/start - Start the bot\n/help - Show this help message")
    else:
        send_message(chat_id, "Unknown command. Type /help to see available commands.")


# Define a function to echo messages or handle commands
def process_update(update):
    chat_id = update["message"]["chat"]["id"]
    if "text" in update["message"]:
        message_text = update["message"]["text"]
        if message_text.startswith('/'):
            handle_command(message_text, chat_id)
        else:
            send_message(chat_id, message_text)


def main():
    offset = None
    while True:
        updates = get_updates(offset)
        for update in updates:
            process_update(update)
            offset = update["update_id"] + 1


def get_updates(offset=None):
    url = BASE_URL + "getUpdates"
    params = {"timeout": 30, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()["result"]

if __name__ == '__main__':
    main()