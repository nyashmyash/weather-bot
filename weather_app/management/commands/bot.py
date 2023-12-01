from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import types
from telebot import TeleBot
from dependency_injector.wiring import inject, Provide
from ...repository import CityRepository
from weather.containers import Container
from weather.services import WeatherService
from weather import container

#container.wire(modules=[__name__])
bot = TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)


class Command(BaseCommand):
    help = 'Запуск бота погоды'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2) # Сохранение обработчиков
        bot.load_next_step_handlers()				# Загрузка обработчиков
        bot.infinity_polling()						# Бесконечный цикл бота


def header_msg(message, text: str):
    user_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    button_weather = types.KeyboardButton(text="Узнать погоду", request_contact=False)
    user_markup.add(button_weather)
    bot.send_message(message.chat.id, text, reply_markup=user_markup)


@bot.message_handler(commands=["start"])
def start(message):
    header_msg(message, "Привет, друг")


@bot.message_handler(content_types=['text'])
@inject
def weather(message,  weather_service: WeatherService = Provide[Container.weather_service],):
    c = CityRepository.get_city(message.text)
    if c:
        #pr = Provide[Container.weather_service]
        weather = weather_service.get_current_weather(c.lat, c.lon)
        out = f'''температура завтра днем {weather["temp"]},
        ветер {weather["wind_speed"]},
        давление {weather["pressure_mm"]}'''
        header_msg(message, out)
    elif message.text == 'Узнать погоду':
        header_msg(message, "Напишите город")
    else:
        header_msg(message, "Не знаю такой команды")
