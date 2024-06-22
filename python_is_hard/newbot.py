import os
import telebot
from dotenv import load_dotenv
from openai import OpenAI
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# загрузка переменных окружения из файла .env

load_dotenv()

# Подгружаем токен телеграмма из .энв

API_TOKEN = os.getenv("TELEBOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)# type: ignore

# запускаем клиент ОпенАИ
client = OpenAI()

# Создаем словарь для хранения контекста диалогов с юзером

bd = {}

# Создается функция для получения ответа от AI на основе контекста диалога
def AI_response(user_id):

    messages = [
        {
            "role": "system",
            "content": "Ты младший брат Джарвиса. Интеллект знающий ответ на любой вопрос, готовый придти на помощь по первому зову.",
        }
    ]
    messages.extend(bd[user_id])

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages, # type: ignore
    )

    return completion.choices[0].message.content

# создаем обработчика команды /start
@bot.message_handler(commands=["start"])
def send_welcome(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.row(InlineKeyboardButton("Lobotomy", callback_data="clear_context"))

    bot.send_message(
        chat_id=message.chat.id,
        text="Если захочешь начать диалог по новой - жми кнопку",
        reply_markup=keyboard,
    )

# Обработчик нажатий на инлайн-кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    if call.data == 'clear_context': # обнуляется контекстдля юзера
        bd[user_id] = []
        bot.send_message(chat_id=chat_id, text='О, привет, чем могу помочь?')
        bot.delete_message(chat_id, message_id)


# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_message(message):

    user_id = message.from_user.id
    message_text = message.text
    chat_id = message.chat.id

    bd[user_id] = bd.get(user_id, [])  # Создаем контекст юзера, если его еще нет
    # Добавляем сообщения юзера в контекст
    bd[user_id].append(
        {
            "role": "user",
            "content": message_text,
        }
    )

    answer = AI_response(user_id) # получаем ответ от АИ
# Добавляем ответ в АИ контекст
    bd[user_id].append(
        {
            "role": "assistant",
            "content": answer,
        }
    )
# отправляем ответ пользователю
    bot.send_message(chat_id=chat_id, text=answer) # type: ignore

# И запускаем бесконечную обработку сообщений
bot.infinity_polling()
