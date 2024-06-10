import telebot
token = "7312344875:AAEvTxC-AEy9u4bc1yua5mqR-g5FePZ2j3s"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Никто тебя не любит. Все тебя ненавидят. Они проиграют. Улыбнись, уёбан.")
bot.infinity_polling
