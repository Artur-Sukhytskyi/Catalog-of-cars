#Catalog-of-cars

Реализовать каталог автомобилей.

ТЗ:
1. Весь проект Django состоит из одного приложения.
2. Необходимо описать модель автомобиля (Car) с полями:
    производитель (BMW, Audi, Tesla и т.д.) (CharField)
    модель авто (S, TT, X6 и т.д.) (CharField)
    год выпуска (IntegerField)
    коробка передач (SmallIntegerField with choices "механика", "автомат", "робот")
    цвет
3. Необходимо создать главную страницу со списком автомобилей.
4. На главной странице создать форму «фильтрации» (поиска) автомобилей.
5. GET-запросом отправлять данные о фильтрах.
6. Во view собирать запрос с помощью Q-объектов и отображать авто на главной с учётом фильтров.

Требования к проекту указаны в файле "requirements.txt"

Для запуска использовать в консоли команду: "python manage.py runserver"

После запуска сервера, проект будет доступен по адресу http://127.0.0.1:8000/

Админка: http://127.0.0.1:8000/admin/

Логин:  admin
пароль: admin

В БД было занесено некоторое количество автомобилей разных производителей и марок с заполнеными годами выпуска, цветом и типом КПП.

В проэкте можно фильтровать каталог по годам выпуска, цвету, типу КПП, а также выполнять поиск по названию и производителю автомобиля

Implement a car catalog.

TT:
1. The entire Django project consists of one application.
2. It is necessary to describe the car model with the fields:
    manufacturer (BMW, Audi, Tesla, etc.) (CharField)
    car model (S, TT, X6, etc.) (CharField)
    year of manufacture (IntegerField)
    gearbox (SmallIntegerField with choices "mechanics", "automatic", "robot")
    Colour
3. It is necessary to create a main page with a list of cars.
4. On the main page, create a form for "filtering" (search) cars.
5. Send filter data with a GET request.
6. In the view, collect the request using Q-objects and display the car on the main page, taking into account filters.

Project requirements are specified in the "requirements.txt" file

To run, use the command in the console: "python manage.py runserver"

After starting the server, the project will be available at http://127.0.0.1:8000/

Admin panel: http://127.0.0.1:8000/admin/

Login: admin
password: admin

A certain number of cars of different manufacturers and brands with complete years of production, color and type of gearbox were entered in the database.

In the project, you can filter the catalog by year of manufacture, color, gearbox type, as well as search by car name and manufacturer
