import telebot

bot = telebot.TeleBot("5717701098:AAE9QWJ-IbMiVNg5rRoVLFXumksYtHTgYno")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "привет бро")


bot.polling(none_stop=True)