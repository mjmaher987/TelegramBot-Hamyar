from telebot import *

token = '6124965342:AAHQfQikY_iGw3lsgrlijpE9XZw7IQCLUMw'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(user_):
    user = user_
    print(user)
    user_id = user.chat.id
    firstname = user.chat.first_name
    lastname = user.chat.last_name
    if firstname is not None and lastname is not None:
        name = firstname + ' ' + lastname
    elif firstname is not None:
        name = firstname
    elif lastname is not None:
        name = lastname
    else:
        name = 'Unknown!'


    bot.send_message(user_id, 'سلام ' + name)
    bot.send_message(user_id, 'امیدوارم حالت خوب باشه.')

    buttons = types.ReplyKeyboardMarkup(row_width=1)
    button_1 = types.KeyboardButton("about_us")
    button_2 = types.KeyboardButton("channel")
    buttons.add(button_1, button_2)
    bot.send_message(user_id, 'چطور میتونم کمکت کنم؟', reply_markup=buttons)



@bot.message_handler(content_types=['text'])
def main(user_):
    user = user_
    print(user)
    entered_command = user.text
    user_id = user.chat.id
    if entered_command == 'channel':
        bot.send_message(user_id, 'https://t.me/SUT_hamyar')
    elif entered_command == 'about_us':
        bot.send_message(user_id, 'https://yek.link/hamyar_sut')


bot.polling()



