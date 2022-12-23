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

main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_work_with_a_cash = types.InlineKeyboardButton("Робота з рахунком")
button_purchase_of_goods = types.InlineKeyboardButton("Купівля товарів")
button_training = types.InlineKeyboardButton("Тренування")
main_keyboard.add(button_work_with_a_cash, button_purchase_of_goods, button_training)

ivan = telebot.TeleBot(config["token"])


@ivan.message_handler(commands=["start"])
def start(message):
    ivan.send_message(message.chat.id,
                      "Вітаємо у системі спортзалу, якщо ви є нашим клієнтом, то пройдіть авторизацію, "
                      "а якщо ні, то ласкаво просимо на реєстрацію", reply_markup=free_access)


@ivan.message_handler(content_types=["text"])
def get_text(message):
    # now_time = time.time()
    # file = open(clients, "r", encoding='utf-8')
    # user_time_all = file.read().split("\n")
    # user_time_all = user_time_all[0:len(user_time_all)-1]
    # file.close()
    if message.text.lower() == "авторизація":
        ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Введіть пароль для входу"),
                                        authorization)
    elif message.text.lower() == "реєстрація":
        ivan.register_next_step_handler(ivan.send_message(message.chat.id, "Придумайте пароль (не менше шести "
                                                                           "символів)"), registration)



def registration(message):
    if len(message.text) < 6:  # Перевіряємо корректність введеного паролю
        ivan.send_message(message.chat.id, "Некорректно введений пароль, повторіть процедуру реєстрації")
    else:
        file = open(clients, "r", encoding='utf-8')
        all_users = file.read().split("\n")
        file.close()
        clients_n, all_users_now = "-", ""
        for elem in range(len(all_users)):
            if message.chat.id == int(
                    all_users[elem].split("/")[0]):  # Перевіряємо чи даний клієнт вже був зареєстрований раніше
                print("Yes")
                all_users[elem] = f"{all_users[elem].split('/')[0]}/{message.text}/{time.time()}/" \
                                  f"{all_users[elem].split('/')[3]}"  # Якщо клієнт є в базі, то просто змінюємо пароль
                for el in all_users:  # Підготовлюємо бд клієнтів для перезапису у файл
                    all_users_now += f"{el}\n"
                file = open(clients, "w", encoding='utf-8')
                file.write(all_users_now[0:len(all_users_now) - 1])
                file.close()
                clients_n = "+"
                break
        if clients_n == "-":  # Якщо клієнта не знайдено у базі, то йго дані просто туди дозаписуємо
            file = open(clients, "a", encoding='utf-8')
            file.write(f"{message.chat.id}/{message.text}/{time.time()}/0\n")
            file.close()
        ivan.send_message(message.chat.id, f"Вітаю, вас успішно зареєстровано у системі, отримайте вашу карту та "
                                           f"авторизуйтесь для входу")


def authorization(message):
    file = open(clients, "r", encoding='utf-8')
    log_pass = file.read().split("\n")
    var = 0
    for ind in range(len(log_pass)):
        if len(log_pass[ind]) > 1:
            if str(log_pass[ind].split("/")[1]) == str(message.text) and message.chat.id == int(
                    log_pass[ind].split("/")[0]):
                ivan.send_message(message.chat.id, "Вітаємо у системі", reply_markup=main_keyboard)
                log_pass[ind] = f"{message.chat.id}/{message.text}/{time.time()}/{log_pass[ind].split('/')[3]}"
                var_var, var = '', 1
                for ind in range(len(log_pass)):
                    var_var += f'{log_pass[ind]}\n'
                file = open(clients, "w", encoding='utf-8')
                file.write(var_var[0:len(var_var) - 1])
                file.close()
                break
    if var == 0:
        ivan.send_message(message.chat.id, f"Невірно введений пароль, або ви не зареєстровані у системиі")


ivan.polling(none_stop=True, interval=0)
