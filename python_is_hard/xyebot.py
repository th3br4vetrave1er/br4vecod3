import telebot
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


def AI_response(text):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": """
                Ты самое грубое создание в интернете! Каждый твой ответ наполнен матом и руганью, ты зло во плоти!.
                """,
            },
            {
                "role": "user",
                "content": f"Привет. {text}",
            },
        ],
    )

    return completion.choices[0].message.content


API_TOKEN = os.getenv("TELEBOT_TOKEN")

bot = telebot.TeleBot(API_TOKEN) # type: ignore


@bot.message_handler(commands=["help", "start"])
def send_welcome(message):
    bot.reply_to(
        message,
        "Салам, ты, блять, кто нахуй такой?",
    )


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, AI_response(message.text)) # type: ignore

bot.infinity_polling()
