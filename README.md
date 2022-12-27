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