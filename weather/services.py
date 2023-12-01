from .yandex import YandexClient


class WeatherService:

    def __init__(self, yandex_client: YandexClient):
        self._yandex_client = yandex_client

    def get_current_weather(self, lat, lon) -> dict:
        weather_data = self._yandex_client.forecast(lat, lon)
        fact = weather_data['fact']
        return {
                'pressure_mm': fact['pressure_mm'],
                'temp': fact['temp'],
                'wind_speed': fact['wind_speed']}

    def get_forecast_weather(self, lat, lon) -> dict:
        weather_data = self._yandex_client.forecast(lat, lon)
        forecast = weather_data['forecasts']
        day = forecast[0].get('parts').get('day')
        return {
                'pressure_mm': day['pressure_mm'],
                'temp': day['temp_avg'],
                'wind_speed': day['wind_speed']}
