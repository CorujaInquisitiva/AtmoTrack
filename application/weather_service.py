from domain.weather import Weather

class WeatherService:
    def create_weather(self, city, temperature, condition, source):
        return Weather(
            city=city,
            temperature_c=temperature,
            condition=condition,
            source=source
        )
