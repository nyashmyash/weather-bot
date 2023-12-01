from dependency_injector import containers, providers

from .yandex import YandexClient
from .services import WeatherService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    yandex_client = providers.Factory(
        YandexClient,
        api_key=config.API_KEY,
        limit=config.LIMIT,
    )
    weather_service = providers.Factory(
        WeatherService,
        yandex_client,
    )

