import telebot
from telebot import types

bot = telebot.TeleBot("5717701098:AAE9QWJ-IbMiVNg5rRoVLFXumksYtHTgYno")

@bot.message_handler(commands=['start'])
def start(message):
    mess = f"hi bro, <b>{message.from_user.first_name}</b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Check it!", url="https://www.meme-arsenal.com/memes/ebe78bb427cea6d882f48cd0331617f9.jpg"))
    bot.send_message(message.chat.id, "Go to link.", reply_markup=markup)


@bot.message_handler()
def get_user_test(message):
    # if message.text == "Hello":

    bot.send_message(message.chat.id, message, parse_mode="html")

bot.polling(none_stop=True)