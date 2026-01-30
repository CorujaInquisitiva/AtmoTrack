from infrastructure.api_client import WeatherAPIClient
from infrastructure.csv_repository import CSVRepository
from application.weather_service import WeatherService

API_KEY = "31fc3d041c89b7ba712231255a740443"

def main():
    city = "São Paulo"

    api_client = WeatherAPIClient(API_KEY)
    service = WeatherService()
    repository = CSVRepository("weather_data.csv")

    try:
        temperature, condition = api_client.fetch_weather(city)

        weather = service.create_weather(
            city=city,
            temperature=temperature,
            condition=condition,
            source="API OpenWeatherMap"
        )

        repository.save([weather])
        print("Dados coletados via API com sucesso.")

    except Exception as e:
        print(f"Erro na API: {e}")

if __name__ == "__main__":
    main()
