import telebot

token = "6130804609:AAFQnNXo9gjzicXZGtcJj251Z-PZd2x6kP0"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    buttonA = telebot.types.InlineKeyboardButton(text='A', callback_data=1)
    buttonB = telebot.types.InlineKeyboardButton(text='B', callback_data=2)
    buttonC = telebot.types.InlineKeyboardButton(text='C', callback_data=3)
    keyboard.add(buttonA, buttonB)
    keyboard.add(buttonC)

    bot.send_message(message.chat.id, 'It works!', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за ответ!')
    answer = ''
    if call.data == '1':
        answer = 'Вы нажали "А"'
    elif call.data == '2':
            answer = 'Вы нажали "B"'
    elif call.data == '3':
        answer = 'Вы нажали "C"'
    bot.send_message(call.message.chat.id, answer)

bot.polling()
