from infrastructure.scraping_client import WeatherScrapingClient
from infrastructure.csv_repository import CSVRepository
from application.weather_service import WeatherService

def main():
    cities = [
        {"city_slug": "sao-paulo", "city_name": "São Paulo", "country": "brazil"},
        {"city_slug": "rio-de-janeiro", "city_name": "Rio de Janeiro", "country": "brazil"},
        {"city_slug": "belo-horizonte", "city_name": "Belo Horizonte", "country": "brazil"},
        {"city_slug": "curitiba", "city_name": "Curitiba", "country": "brazil"},
        {"city_slug": "porto-alegre", "city_name": "Porto Alegre", "country": "brazil"}
    ]

    scraping_client = WeatherScrapingClient()
    service = WeatherService()
    repository = CSVRepository("weather_data.csv")

    weather_data = []

    for city_info in cities:
        try:
            temperature, condition = scraping_client.fetch_weather(city_info["country"], city_info["city_slug"])

            weather = service.create_weather(
                city=city_info["city_name"],
                temperature=temperature,
                condition=condition,
                source="Web Scraping"
            )

            weather_data.append(weather)
            print(f"Dados coletados para {city_info['city_name']} com sucesso.")

        except Exception as e:
            print(f"Erro no scraping para {city_info['city_name']}: {e}")

    if weather_data:
        repository.save(weather_data)
        print("Todos os dados foram salvos no CSV.")

if __name__ == "__main__":
    main()
