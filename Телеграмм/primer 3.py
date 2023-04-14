import telebot

token = "6130804609:AAFQnNXo9gjzicXZGtcJj251Z-PZd2x6kP0"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(func=lambda x: len(x.text) == 3)
def alf_three_message(message): bot.send_message(message.chat.id, 'Это слова из 3-х букв')

@bot.message_handler(func=lambda x: x.text in ['привет', 'здравствуй'])
def greeting_message(message):
    bot.send_message(message.chat.id, 'Привет! Рад снова тебя приветсвовать!')

@bot.message_handler(func=lambda x: True)
def other_message(message):
    bot.send_message(message.chat.id, 'Я тебя услышал')

bot.polling()
