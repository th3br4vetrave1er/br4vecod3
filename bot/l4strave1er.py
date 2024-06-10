import os
from dotenv import load_dotenv
import telebot
import schedule
import time
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
  bot.send_message(message.chat.id,"Ещё не время...")
  
  
def send_daily_message():
    chat_id = 'bravetrave1er'  # Замени на свой chat_id
    bot.send_message(chat_id, "Никто тебя не любит. Все тебя ненавидят. Они проиграют. Улыбнись, уёбан.")
    
    
schedule.every().day.at("12:12").do(send_daily_message)

# Функция для запуска планировщика в отдельном потоке
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Запуск планировщика
import threading
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()

bot.infinity_polling()