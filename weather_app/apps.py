from django.apps import AppConfig
from weather import container


class WeatherAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather_app'

    def ready(self):
        container.wire(modules=[".views", ".management.commands.bot"])

