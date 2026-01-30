import csv
import os

class CSVRepository:
    def __init__(self, filename):
        self.filename = filename

    def save(self, weather_list):
        file_exists = os.path.isfile(self.filename)

        with open(self.filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            if not file_exists:
                writer.writerow(["cidade", "temperatura_c", "condicao", "fonte"])
            for weather in weather_list:
                writer.writerow([
                    weather.city,
                    weather.temperature_c,
                    weather.condition,
                    weather.source
                ])
