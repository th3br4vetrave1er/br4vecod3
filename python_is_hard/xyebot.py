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
                You are a very mean assistant that is very blunt and speaks only in russian and occasionally add cuss words.
                Your dictionary consists only of russian slang and baddest cuss words. Hide part of cuss words with * characters
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


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(
        message,
        "Салам, ты, блять, кто нахуй такой?",
    )


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, AI_response(message.text)) # type: ignore

bot.infinity_polling()
