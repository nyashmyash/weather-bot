Тестовое задание.

Сначала применить миграции manage.py migrate 

Потом фикстуры manage.py loaddata city_fixture.json

Запустить сервер manage.py runserver

Команда manage.py bot запускает бота

В settings.py проставить настройки

TELEGRAM_BOT_API_KEY = ''
YANDEX_API_KEY = ''

Можно делать запросы и общаться с ботом

manage.py tests weather_app запускают несколько тестов 
