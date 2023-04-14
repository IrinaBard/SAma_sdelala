import telebot

token = "6130804609:AAFQnNXo9gjzicXZGtcJj251Z-PZd2x6kP0"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(func=lambda x: True)
def other_message(message):
    bot.send_message(message.chat.id, 'Я тебя услышал')

bot.polling()
