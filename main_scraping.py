from infrastructure.scraping_client import WeatherScrapingClient
from infrastructure.csv_repository import CSVRepository
from application.weather_service import WeatherService

def main():
    city = "sao-paulo"
    country = "brazil"

    scraping_client = WeatherScrapingClient()
    service = WeatherService()
    repository = CSVRepository("weather_data.csv")

    try:
        temperature, condition = scraping_client.fetch_weather(country, city)

        weather = service.create_weather(
            city="São Paulo",
            temperature=temperature,
            condition=condition,
            source="Web Scraping"
        )

        repository.save([weather])
        print("Dados coletados via scraping com sucesso.")

    except Exception as e:
        print(f"Erro no scraping: {e}")

if __name__ == "__main__":
    main()
