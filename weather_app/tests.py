import unittest
from unittest import mock

from django.test import TestCase

from .models import City
import json
import decimal


from weather.yandex import YandexClient
from weather.services import WeatherService


class CityModelTestCase(TestCase):
    fixtures = ['city_fixture.json']

    def setUp(self):
        pass

    def test_get_data(self):
        obj = City.objects.get(name="Владивосток")
        self.assertEqual(obj.lon, round(decimal.Decimal(43.11000), 5))
        self.assertEqual(obj.lat, round(decimal.Decimal(131.87000), 5))

    def test_fail_get_data(self):
        reslt = City.objects.filter(name="Владив")
        self.assertEqual(len(reslt), 0)


class YandexTestCase(TestCase):
    fixtures = ['city_fixture.json']

    def setUp(self):
        pass

    def test_weather_data(self):
        with open('test.json', 'r') as file:
            json_data = json.load(file)
            yandex_client_mock = mock.Mock(spec=YandexClient)
            yandex_client_mock.forecast.return_value = json_data
            ws = WeatherService(yandex_client_mock)

            data = ws.get_current_weather(55.7, 37.6)
            self.assertEqual(data, {
                'pressure_mm': 725,
                'temp': 2,
                'wind_speed': 5.9})

    def test_forecast_get_data(self):
        with open('test.json', 'r') as file:
            json_data = json.load(file)
            yandex_client_mock = mock.Mock(spec=YandexClient)
            yandex_client_mock.forecast.return_value = json_data
            ws = WeatherService(yandex_client_mock)
            data = ws.get_forecast_weather(55.7, 37.6)
            self.assertEqual(data, {
                'pressure_mm': 725,
                'temp': 3,
                'wind_speed': 6.1})

    def test_weather_fail(self):
        with open('test.json', 'r') as file:
            json_data = json.load(file)
            yandex_client_mock = mock.Mock(spec=YandexClient)
            yandex_client_mock.forecast.return_value = json_data
            ws = WeatherService(yandex_client_mock)
            data = ws.get_current_weather(55.7, 37.6)
            self.assertNotEqual(data, {
                'pressure_mm': 726,
                'temp': 5,
                'wind_speed': 6.9})

    def test_forecast_fail(self):
        with open('test.json', 'r') as file:
            json_data = json.load(file)
            yandex_client_mock = mock.Mock(spec=YandexClient)
            yandex_client_mock.forecast.return_value = json_data
            ws = WeatherService(yandex_client_mock)
            data = ws.get_forecast_weather(55.7, 37.6)
            self.assertNotEqual(data, {
                'pressure_mm': 732,
                'temp': -3,
                'wind_speed': 8.6})


if __name__ == '__main__':
    unittest.main()
