import telebot

token = "6130804609:AAFQnNXo9gjzicXZGtcJj251Z-PZd2x6kP0"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    buttonA = telebot.types.KeyboardButton('Avv')
    buttonB = telebot.types.KeyboardButton('Bff')
    buttonC = telebot.types.KeyboardButton('Cdd')

    keyboard.add(buttonA, buttonB)
    keyboard.add(buttonC)
    bot.send_message(message.chat.id, 'It works!', reply_markup=keyboard)

@bot.message_handler(func=lambda x: True)
def other_message(message):
    bot.send_message(message.chat.id, 'Ты напечатал: ' + message.text)
bot.polling()
