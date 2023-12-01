import requests


class YandexClient:
    API_URL = "https://api.weather.yandex.ru/v2"

    def __init__(self, api_key, limit):
        self._api_key = api_key
        self._limit = limit

    def forecast(self, lat, lon):
        """Make search API call and return result."""
        url = f"{self.API_URL}/forecast"
        params = {
            "lat": lat,
            "lon": lon,
            "limit": self._limit
        }
        headers = {'X-Yandex-API-Key': self._api_key, }

        return requests.get(url, headers=headers, params=params).json()
