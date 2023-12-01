# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.views.decorators.cache import cache_page
from dependency_injector.wiring import inject, Provide
from weather.containers import Container
from weather.services import WeatherService
from .repository import CityRepository


@inject
@cache_page(60 * 30)  # кешировать ответ на 30 минут
def get_weather(request: HttpRequest,
                weather_service: WeatherService = Provide[Container.weather_service], ) -> HttpResponse:
    city = request.GET.get('city', "")
    c = CityRepository.get_city(city)
    if not c:
        return HttpResponse(str({'error': 'Город не указан'}))

    return HttpResponse(content=str(weather_service.get_current_weather(c.lat, c.lon)))
