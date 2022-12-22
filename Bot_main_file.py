import telebot
import os.path
from telebot import types

path = os.path.join("Data_baseata_base", "Clients.txt")

config = {
    "name": "Python_waran_bot",
    "token": "5737862312:AAEjHoaa-Gzxr3JbJx6TzRzBu32Q3NbbppY"
}

free_access = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_registration = types.InlineKeyboardButton("реєстрація")
button_authorization = types.InlineKeyboardButton("авторизація")
free_access.add(button_registration, button_authorization)

ivan = telebot.TeleBot(config["token"])


@ivan.message_handler(commands=["start"])
def start(message):
    ivan.send_message(message.chat.id,
                      "Вітаємо у системі спортзалу, якщо ви є нашим клієнтом, то пройдіть авторизацію, "
                      "а якщо ні, то ласкаво просимо на реєстрацію", reply_markup=free_access)







ivan.polling(none_stop=True, interval=0)