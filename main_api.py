from infrastructure.api_client import WeatherAPIClient
from infrastructure.csv_repository import CSVRepository
from application.weather_service import WeatherService

API_KEY = "31fc3d041c89b7ba712231255a740443"

def main():
    cities = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre"]

    api_client = WeatherAPIClient(API_KEY)
    service = WeatherService()
    repository = CSVRepository("weather_data.csv")

    weather_data = []

    for city in cities:
        try:
            temperature, condition = api_client.fetch_weather(city)

            weather = service.create_weather(
                city=city,
                temperature=temperature,
                condition=condition,
                source="API OpenWeatherMap"
            )

            weather_data.append(weather)
            print(f"Dados coletados para {city} com sucesso.")

        except Exception as e:
            print(f"Erro na API para {city}: {e}")

    if weather_data:
        repository.save(weather_data)
        print("Todos os dados foram salvos no CSV.")

if __name__ == "__main__":
    main()
