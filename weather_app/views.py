# Create your views here.
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

from .yandex.api_weather import get_req_yandex
from .yandex.json_manager import get_current_weather


@cache_page(60 * 30)  # кешировать ответ на 30 минут
def get_weather(request) -> HttpResponse:
    city = request.GET.get('city', "")

    if city == '':
        return HttpResponse(str({'error': 'Город не указан'}))
    response = get_req_yandex(city)
    if not response:
        return HttpResponse(str({'error': 'Город не указан'}))
    if response.status_code == 200:
        # Обработка полученных данных
        return HttpResponse(content=str(get_current_weather(response.json())))
    else:
        return HttpResponse(str({'error': 'Ошибка в получении данных'}))
