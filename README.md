# Телеграм бот для тренажерного комплексу

### Запуск бота
* Відбувається шляхом запуску файлу "Bot_main_file.py"

### Даний телеграм бот реалізує функції:
* __Вхід-реєстрація клієнта:__
  * Реєстрація нового клієнта після виборю відповідної опції та вводу бажаного пароля 
    (мінімум 6 символів)(данні клієнта заносяться у файл "Clients.txt"), при цьому створюється рахунок для витрат всередені комплексу
  * Авторизіція користувача після вибору відповідної опції та вводу пароля
  * Переавторизація користувача, якщо з моменту його попередньої авторизації
    минуло більше доби
* __Робота з внутрішнім рахунком для використання всередині комплексу:__
  * Перевірка поточного стану внутрішнього рахунку
  * Опція поповнення внутрішнього рахунку комплексу
  * Повернення у основне меню
* __Купівля товару:__
  * При вибору опції купівлі товарів у меню можна обрати: 
    * Купівлю абонементів на тренування;
    * Обрати один з наявних товарів (перелік підтягується з окремого файлу "Shop.txt"), після чого він додається у 
      кошик (вноситься у файл "User_product.json");
    * Переглянути залишок на внутрішньому рахунку;
    * Перегляд товарів вже доданих у кошик;
    * Проведення оплати за обрані товари з кошику;
    * Очищення кошика
* __Вкладка Тренування:__
  * Перелік тренерів наявних тренерів (перелік яких підтягується з файлу "Treiner_all.json");
    * При обранні бажаного тренера виводиться розклад на тиждень з вільними годинами для тренувань, натиснувши на 
      обраний час клвєнт записує себе на тренування (підтягується з файлу "Treiner.json");
    * Перегляд розкладу ваших тренувань з обраними тренерами
### Файли проекту:
* Папка "Data_base":
  * "Clients.txt" - файл з данними про клієнтів;
  * "Shop.txt" - файл з переліком доступних товарів у внутрішньому магазині;
  * "Treiner.json" - файл з розкладом тренувань на тиждень для тренерів та клієнтів;
  * "Treiner_all.json" - файл з переліком тренерів
  * "User_product.json" - файл-кошик з товарами, обраними клієнтом для купівлі
* "Bot_main_file.py" - стартовий та основний файл проекту
* "README.md" - файл з описом проекту
* "Telegram_bot_map1.jpg" - схема проекту



# Telegram bot for the training complex

### Starting the bot
* Occurs by running the file "Bot_main_file.py"

### This Telegram bot implements the following functions:
* __Client login-registration:__
  * Registration of a new client after selecting the appropriate option and entering the desired password
    (minimum 6 characters) (client data is entered in the "Clients.txt" file), while an account is created for expenses within the complex
  * User authorization after selecting the appropriate option and entering a password
  * Reauthorization of the user, if from the moment of his previous authorization
    more than a day has passed
* __Working with an internal account for use within the complex:__
  * Checking the current state of the internal account
  * Option to replenish the complex's internal account
  * Return to the main menu
* __Purchase of goods:__
  * When choosing the option to buy goods in the menu, you can choose:
    * Purchase of subscriptions for training;
    * Select one of the available products (the list is pulled from a separate "Shop.txt" file), after which it is added to
      shopping cart (entered in the "User_product.json" file);
    * View the balance on the internal account;
    * View products already added to the cart;
    * Payment for selected goods from the basket;
    * Cleaning the basket
* __Tab Training:__
  * The list of available trainers (the list of which is pulled from the "Treiner_all.json" file);
    * When selecting the desired trainer, a schedule for a week with free hours for training is displayed by clicking on
      at the selected time, the client registers himself for training (pulled from the "Treiner.json" file);
    * View your training schedule with selected trainers
### Project files:
* "Data_base" folder:
  * "Clients.txt" - a file with data about clients;
  * "Shop.txt" - a file with a list of available products in the internal store;
  * "Treiner.json" - file with weekly training schedule for trainers and clients;
  * "Treiner_all.json" - a file with a list of trainers
  * "User_product.json" is a shopping cart file with products selected by the client for purchase
* "Bot_main_file.py" - the starting and main file of the project
* "README.md" is a project description file
* "Telegram_bot_map1.jpg" - the scheme of the project