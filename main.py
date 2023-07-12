from telebot import *
import mysql.connector
import os
from datetime import date

token = '6124965342:AAHQfQikY_iGw3lsgrlijpE9XZw7IQCLUMw'
bot = telebot.TeleBot(token)

polling_state = "None"

def init_dB():

    global dB
    dB = mysql.connector.connect(
      host="MOHSH.mysql.pythonanywhere-services.com",
      user="MOHSH",
      password="SutHamyarDB",
      database="MOHSH$SUT-Hamyar-Bot"
    )

    global cursor
    cursor = dB.cursor()

def is_admin(user_id):

    admins = cursor.execute("SELECT * FROM AdminsList")
    admins_list = []

    for item in cursor.fetchall():
      admins_list.append(item[0])

    return user_id in admins_list

def add_user_menu(user_id):
    
    buttons = types.ReplyKeyboardMarkup(row_width=2)
    button_1 = types.KeyboardButton("درباره ما")
    button_2 = types.KeyboardButton("پیشنهادات و انتقادات")
    button_3 = types.KeyboardButton("یادآور رویدادها")
    button_4 = types.KeyboardButton("کانال همیاران سلامت و روان")
    buttons.add(button_1, button_2, button_3, button_4)
    bot.send_message(user_id, 'چطور میتونم کمکت کنم؟', reply_markup=buttons)

def add_admin_menu(user_id):
    
    buttons = types.ReplyKeyboardMarkup(row_width=2)
    button_1 = types.KeyboardButton("درباره ما")
    button_2 = types.KeyboardButton("پیشنهادات و انتقادات")
    button_3 = types.KeyboardButton("یادآور رویدادها")
    button_4 = types.KeyboardButton("کانال همیاران سلامت و روان")
    button_5 = types.KeyboardButton("نمایش پیشنهادات و انتقادات")
    button_6 = types.KeyboardButton("ایجاد رویداد")
    buttons.add(button_1, button_2, button_3, button_4, button_5, button_6)
    bot.send_message(user_id, 'چطور میتونم کمکت کنم؟', reply_markup=buttons)

def event_subscribe(user):
    cursor.execute("INSERT INTO Subscribers (id) VALUES (%s)", (user.chat.id, ))
    bot.send_message(user.chat.id, "از این به بعد برای هر کدوم از رویداد های کانون برای شما پیام یادآور می فرستیم.")
    
def show_Feedbacks(user):
    cursor.execute("SELECT * FROM Feedbacks")
    data = "پیشنهادات : \n"
    for item in cursor.fetchall():
      data += "تاریخ : " + item[0] + " , " + "پیشنهاد : " + item[1] + "\n===============\n"
    bot.send_message(user.chat.id, data)
    
def send_Feedback(user):
    bot.send_message(user.chat.id, "هر چه دل تنگت می خواهت بگو :)")
    global polling_state
    polling_state = "User feedback"
    
def parse_user_feedback(user):
    bot.send_message(user.chat.id, "از اینکه به ما در بهتر کردن کانال و بات کمک می کنی ممنونیم 🙏")
    global polling_state
    polling_state = "None"
    msg = user.text
    time = date.today()
    cursor.execute("INSERT INTO Feedbacks (time, content) VALUES (%s, %s)", (time, msg))
    
admins = [100, 200, 1047965559000]


@bot.message_handler(commands=['start'])
def start(user_):
    user = user_
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

    init_dB()
    
    bot.send_message(user_id, 'سلام ' + name)
    bot.send_message(user_id, 'امیدوارم حالت خوب باشه.')

    if is_admin(user_id):
    # if user_id in admins:
        add_admin_menu(user_id)
    else:
        add_user_menu(user_id)
    

@bot.message_handler(content_types=['text'])
def main(user_):
    user = user_
    entered_command = user.text
    user_id = user.chat.id
    
    if polling_state == "User feedback":
        parse_user_feedback(user)
        
    if entered_command == 'نمایش پیشنهادات و انتقادات':
        show_Feedbacks(user)
    elif entered_command == 'درباره ما':
        bot.send_message(user_id, 'https://yek.link/hamyar_sut')
    elif entered_command == 'پیشنهادات و انتقادات':
        send_Feedback(user)
    elif entered_command == 'یادآور رویدادها':
        event_subscribe(user)
    elif entered_command == 'کانال همیاران سلامت و روان':
        bot.send_message(user_id, 'https://t.me/SUT_hamyar')

bot.polling()



