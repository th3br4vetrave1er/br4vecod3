import telebot
bot = telebot.TeleBot()


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Никто тебя не любит. Все тебя ненавидят. Они проиграют. Улыбнись, уёбан.")
bot.infinity_polling
