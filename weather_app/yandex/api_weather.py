import requests
from django.conf import settings
from ..models import City

def get_url_weather(lat: float, lon:float, limit: int):
    return f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&lang=ru_RU&limit={limit}&hours=false&extra=false"


def get_req_yandex(city):
    try:
        c = City.objects.get(name=city)
    except City.DoesNotExist:
        return None
    api_key = settings.YANDEX_API_KEY
    limit = 1
    headers = {'X-Yandex-API-Key': api_key,}
    url = get_url_weather(c.lon, c.lat, limit)
    return requests.get(url, headers=headers)
