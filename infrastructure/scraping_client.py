import requests
from bs4 import BeautifulSoup

class WeatherScrapingClient:
    BASE_URL = "https://www.timeanddate.com/weather/"

    def fetch_weather(self, country, city):
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; WeatherBot/1.0)"
        }

        url = f"{self.BASE_URL}{country}/{city}"
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        temp = soup.find("div", class_="h2").text.replace("°C", "")
        condition = soup.find("p").text

        return float(temp), condition
