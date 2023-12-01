Тестовое задание.

Сначала применить миграции manage.py migrate 

Потом фикстуры manage.py loaddata city_fixture.json

Запустить сервер manage.py runserver

Команда manage.py bot запускает бота

В settings.py проставить настройки

TELEGRAM_BOT_API_KEY = '' ключ бота телеграмм
API_KEY = '' для Яндекса
LIMIT = 1 выборка из прогнозов

Можно делать запросы и общаться с ботом

manage.py test weather_app.tests запускают несколько тестов 
