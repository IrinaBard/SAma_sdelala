import telebot

token = ""
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    buttonA = telebot.types.KeyboardButton('A')
    buttonB = telebot.types.KeyboardButton('B')
    buttonC = telebot.types.KeyboardButton('C')

    keyboard.row(buttonA, buttonB)
    keyboard.row(buttonC)
