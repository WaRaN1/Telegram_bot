import telebot
import os.path
from telebot import types
import time

clients = os.path.join("Data_base", "Clients.txt")

config = {
    "name": "Python_waran_bot",
    "token": "5737862312:AAEjHoaa-Gzxr3JbJx6TzRzBu32Q3NbbppY"
}

free_access = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_registration = types.InlineKeyboardButton("Реєстрація")
button_authorization = types.InlineKeyboardButton("Авторизація")
free_access.add(button_registration, button_authorization)

ivan = telebot.TeleBot(config["token"])


@ivan.message_handler(commands=["start"])
def start(message):
    ivan.send_message(message.chat.id,
                      "Вітаємо у системі спортзалу, якщо ви є нашим клієнтом, то пройдіть авторизацію, "
                      "а якщо ні, то ласкаво просимо на реєстрацію", reply_markup=free_access)

@ivan.message_handler(content_types=["text"])
def get_text(message):
    now_time = time.time()

    file = open(clients, "r", encoding='utf-8')
    now_users = file.read().split("\n")
    file.close()

    if message.text.lower() == "авторизація":
        ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Введіть ваше ім'я та пароль через '/' для "
                                                                           "вхoду у систему чатбота"), authorization)
    elif message.text.lower() == "реєстрація":
        ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Введіть ваше ім'я та пароль через "
                                                                           "'/'"), registration)


def registration(message):                                  # Реєстрація у системі
    file = open(clients, "r", encoding='utf-8')
    all_users = file.read().split("\n")
    file.close()
    rez = message.text.split("/")
    var_var = 0
    for el in all_users:                                    # Перевірка чи такий користувач вже зареєстрований
        var = el.split("/")
        if var[0] == rez[0]:
            var_var = 1
            break
    if var_var == 0:
        nowtime = time.time()
        file = open(clients, "a", encoding='utf-8')
        file.write(f"{message.text}/{nowtime}\n")
        file.close()
        ivan.send_message(message.chat.id, f"Вітаю {rez[0]}, вас успішно зареєстровано у системі ")
    else:
        ivan.send_message(message.chat.id, f"Щось пішло не так. Користувач {rez[0]} вже зареєстрований у системі")


def authorization(message):
    file = open(path, "r", encoding='utf-8')
    log_pass = file.read().split("\n")
    rez = text.split("/")
    var = 0
    for ind in range(len(log_pass)+1):
        log_pass[ind] = log_pass[ind].split('/')
        if rez[0] == log_pass[ind][0] and rez[1] == log_pass[ind][1]:
            ivan.send_message(message.chat.id, f"{rez[0]}, вітаємо у системі", reply_markup=keyboard)
            global nameUser
            nameUser = f"{rez[0]}"
            var, old = 1, time.time()
            log_pass[ind] = f'{log_pass[ind][0]}/{log_pass[ind][1]}/{message.chat.id}/{old}'
            var_var = ''
            print(log_pass)
            for ind in range(len(log_pass)):
                var_var += f'{log_pass[ind]}\n'
            file = open(path, "w", encoding='utf-8')
            file.write(var_var)
            file.close()
            break
    if var == 0:
        ivan.send_message(message.chat.id, f"Невірно введені логін або пароль.")

ivan.polling(none_stop=True, interval=0)