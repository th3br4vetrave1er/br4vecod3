import os
from dotenv import load_dotenv
import telebot

# # Загружаем переменные из .env файла
# load_dotenv()

# # Получаем токен из переменной окружения
# TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# # Проверяем, что токен загружен правильно
# if not TOKEN:
#     raise ValueError("No TOKEN found in environment variables")

# bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['start'])
# def handle_start(message):
#     bot.send_message(message.chat.id, "Никто тебя не любит. Все тебя ненавидят. Они проиграют. Улыбнись, уёбан.")

# bot.polling(none_stop=True)

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Никто тебя не любит. Все тебя ненавидят. Они проиграют. Улыбнись, уёбан.")
  

@bot.message_handler(commands=['next'])
def next_messagee(message):
  if message.text=="next":
        bot.send_message(message.chat.id,"Дальше только ты..")
  

bot.infinity_poling()