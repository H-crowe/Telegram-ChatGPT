
# ChatGPT Telegram Bot
# A simple powerful Telegram bot that engages users in interactive conversations using OpenAI's ChatGPT language model.
# Author: H-crowe
# Repository: https://github.com/H-crowe/Telegram-ChatGPT

# Import the necessary libraries
import telebot
import requests
import json
import os
import logging
from telebot import types  # Import the types module for ReplyKeyboardMarkup

# Configure logging
logging.basicConfig(level=logging.INFO)

# configuration from JSON file
try:
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    TELEGRAM_BOT_TOKEN = config.get('TELEGRAM_BOT_TOKEN')
    OPENAI_API_KEY = config.get('OPENAI_API_KEY')

except FileNotFoundError:
    logging.error("Error: Configuration file 'config.json' not found.")
    exit(1)
except json.JSONDecodeError:
    logging.error("Error: Invalid JSON format in the configuration file.")
    exit(1)
except Exception as e:
    logging.error(f"Error: An unexpected error occurred - {e}")
    exit(1)

# Initialize the Telegram bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Define the endpoint URL for the ChatGPT API
chatgpt_api_url = 'https://api.openai.com/v1/engines/davinci-codex/completions'

# Define a dictionary to store user conversations
user_conversations = {}

# Define a function to interact with ChatGPT
def chat_with_gpt(input_text, conversation_id):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}'
    }

    # conversation history
    conversation = user_conversations.get(conversation_id, [])
    conversation.append({'role': 'user', 'content': input_text})

    payload = {
        'messages': conversation,
        'max_tokens': 50
    }

    response = requests.post(chatgpt_api_url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        chatgpt_response = data['choices'][0]['message']['content']
        conversation.append({'role': 'assistant', 'content': chatgpt_response})
        user_conversations[conversation_id] = conversation
        return chatgpt_response
    else:
        logging.error("Error: ChatGPT API request failed")
        return "Error: ChatGPT API request failed"

# Define a command handler function
@bot.message_handler(commands=['start', 'restart', 'help'])
def handle_commands(message):
    user_input = message.text
    if user_input == '/start':
        send_welcome(message)
    elif user_input == '/restart':
        send_restart(message)
    elif user_input == '/help':
        send_help(message)
    

# Define a handler for user messages
@bot.message_handler(func=lambda message: True)
def chat_with_user(message):
    user_input = message.text
    chatgpt_response = chat_with_gpt(user_input, message.chat.id)
    bot.reply_to(message, chatgpt_response)

# Function to send a welcome message
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    item_start = types.KeyboardButton('/start')
    item_restart = types.KeyboardButton('/restart')
    item_help = types.KeyboardButton('/help')
    
    markup.add(item_start, item_help, item_restart)

    bot.reply_to(message, "Welcome to your ChatGPT-powered Telegram Bot! You can start chatting with me.",
                 reply_markup=markup)

# Function to send help message
def send_help(message):
    bot.reply_to(message, "This is a ChatGPT-powered bot. You can start a conversation by sending a message.")

# Function to send restart message
def send_restart(message):
    bot.reply_to(message, "The conversation has been restarted.")

# Start the bot
bot.polling()
