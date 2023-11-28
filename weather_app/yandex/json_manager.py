class Weather:
    pressure = ""
    temp = ""
    wind_speed = ""


def get_current_weather(weather_data: dict) -> dict:
    fact = weather_data['fact']
    return {
            'pressure_mm': fact['pressure_mm'],
            'temp': fact['temp'],
            'wind_speed': fact['wind_speed']}


def get_forecast_weather(weather_data: dict) -> dict:
    forecast = weather_data['forecasts']
    day = forecast[0].get('parts').get('day')
    return {
            'pressure_mm': day['pressure_mm'],
            'temp': day['temp_avg'],
            'wind_speed': day['wind_speed']}

