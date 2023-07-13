from telebot import *
import mysql.connector
import os
from datetime import date

token = ''
bot = telebot.TeleBot(token)

polling_state = "None"
admin_ = None
event_name = None
time_submitted = None


def init_dB():

    global dB
    dB = mysql.connector.connect(
      host="MOHSH.mysql.pythonanywhere-services.com",
      user="MOHSH",
      password="",
      database="MOHSH$SUT-Hamyar-Bot"
    )

    global cursor
    cursor = dB.cursor()


def close_dB():
    dB.commit()
    cursor.close()
    dB.close()

def is_admin(user_id):

    init_dB()
    admins = cursor.execute("SELECT * FROM AdminsList")
    admins_list = []

    for item in cursor.fetchall():
      admins_list.append(item[0])

    close_dB()
    return user_id in admins_list

def add_user_menu(user_id):

    buttons = types.ReplyKeyboardMarkup(row_width=2)
    button_1 = types.KeyboardButton("درباره ما")
    button_2 = types.KeyboardButton("پیشنهادات و انتقادات")
    button_3 = types.KeyboardButton("یادآور رویدادها")
    button_4 = types.KeyboardButton("کانال همیاران سلامت و روان")
    button_5 = types.KeyboardButton("حذف از لیست دریافت پیام یادآور")
    buttons.add(button_1, button_2, button_3, button_4, button_5)
    bot.send_message(user_id, 'چطور میتونم کمکت کنم؟', reply_markup=buttons)

def add_admin_menu(user_id):

    buttons = types.ReplyKeyboardMarkup(row_width=2)
    button_1 = types.KeyboardButton("درباره ما")
    button_2 = types.KeyboardButton("پیشنهادات و انتقادات")
    button_3 = types.KeyboardButton("یادآور رویدادها")
    button_4 = types.KeyboardButton("کانال همیاران سلامت و روان")
    button_5 = types.KeyboardButton("نمایش پیشنهادات و انتقادات")
    button_6 = types.KeyboardButton("ایجاد رویداد")
    button_7 = types.KeyboardButton("حذف لیست پیشنهادات")
    button_8 = types.KeyboardButton("حذف از لیست دریافت پیام یادآور")
    buttons.add(button_1, button_2, button_3, button_4,
                button_5, button_6, button_7, button_8)
    bot.send_message(user_id, 'چطور میتونم کمکت کنم؟', reply_markup=buttons)

def event_subscribe(user):
    init_dB()
    cursor.execute("INSERT INTO Subscribers (id) VALUES (%s)", (user.chat.id, ))
    close_dB()
    bot.send_message(user.chat.id, "از این به بعد برای هر کدوم از رویداد های کانون برای شما پیام یادآور می فرستیم.")

def show_Feedbacks(user):
    init_dB()
    cursor.execute("SELECT * FROM Feedbacks")
    data = "پیشنهادات : \n"
    for item in cursor.fetchall():
      data += "تاریخ : " + item[0] + " \n " + "پیشنهاد : " + item[1] + "\n================================\n"
    bot.send_message(user.chat.id, data)

def send_Feedback(user):
    bot.send_message(user.chat.id, "هر چه دل تنگت می خواهت بگو :)")
    global polling_state
    polling_state = "User feedback"

def send_event(user):
    bot.send_message(user.chat.id, "نام رویداد رو لطفا بفرست")
    global polling_state
    polling_state = "Admin Submit Name of Event"

def receive_event_name(user):
    bot.send_message(user.chat.id, "نام رویداد دریافت شد، حالا لطفا زمان و تاریخ رویداد رو وارد کن")
    global polling_state
    polling_state = "Admin Submit Time of Event"
    event_ = user.text
    time_ = date.today()
    global time_submitted
    global event_name
    time_submitted = time_
    event_name = event_

def receive_event_time(user):
    bot.send_message(user.chat.id, "زمان رویداد هم دریافت شد، ممنونم")
    global polling_state
    global time_submitted
    global event_name
    polling_state = "None"
    event_time = user.text
    init_dB()
    cursor.execute("INSERT INTO Events (time_submitted, event_name, event_time) VALUES (%s, %s, %s)", (time_submitted, event_name, event_time))
    close_dB()

def parse_user_feedback(user):
    bot.send_message(user.chat.id, "از اینکه به ما در بهتر کردن کانال و بات کمک می کنی ممنونیم 🙏")
    global polling_state
    polling_state = "None"
    msg = user.text
    time = date.today()
    init_dB()
    cursor.execute("INSERT INTO Feedbacks (time, content) VALUES (%s, %s)", (time, msg))
    close_dB()

def unsubscribe(user):
    init_dB()
    subs = cursor.execute("SELECT * FROM Subscribers")
    subs_list = []

    for item in cursor.fetchall():
      subs_list.append(item[0])

    if user.chat.id in subs_list:
        cursor.execute("DELETE FROM Subscribers WHERE id = %s", (user.chat.id, ))
        bot.send_message(user.chat.id, "دیگر برای شما پیام یادآور نمی فرستیم.")
    else:
        bot.send_message(user.chat.id, "شما برای دریافت یادآور از قبل درخواست نداده اید.")
    close_dB()

def clear_feedback_dB(user):
    init_dB()
    cursor.execute("DELETE FROM Feedbacks")
    close_dB()
    bot.send_message(user.chat.id, "لیست پیشنهادات با موفقیت پاک شد.")

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
    print('hi')
    print(user_id)

    bot.send_message(user_id, 'سلام ' + name)
    bot.send_message(user_id, 'امیدوارم حالت خوب باشه.')

    if is_admin(user_id):
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
    elif polling_state == "Admin Submit Name of Event":
        receive_event_name(user)
    elif polling_state == "Admin Submit Time of Event": #  and user.chat.id == admin_.chat.id
        receive_event_time(user)
    elif entered_command == 'نمایش پیشنهادات و انتقادات' and is_admin(user_id):
        show_Feedbacks(user)
    elif entered_command == 'درباره ما':
        bot.send_message(user_id, 'https://yek.link/hamyar_sut')
    elif entered_command == 'پیشنهادات و انتقادات':
        send_Feedback(user)
    elif entered_command == 'یادآور رویدادها':
        event_subscribe(user)
    elif entered_command == 'کانال همیاران سلامت و روان':
        bot.send_message(user_id, 'https://t.me/SUT_hamyar')
    elif entered_command == 'حذف لیست پیشنهادات' and is_admin(user_id):
        clear_feedback_dB(user)
    elif entered_command == 'ایجاد رویداد' and is_admin(user_id):
        send_event(user)
    elif entered_command == 'حذف از لیست دریافت پیام یادآور':
        unsubscribe(user)

bot.polling()



