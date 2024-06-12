import telebot

TOKEN = "7312344875:AAEvTxC-AEy9u4bc1yua5mqR-g5FePZ2j3s"
bot = telebot.TeleBot(TOKEN) # Cвязываем код с токеном





@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)










# Запускаем бота в режиме опроса серверов тг на какое-т осообщение. Бот уже висит в онлайне.
if __name__ == "__main__":
    bot.infinity_polling    
    
