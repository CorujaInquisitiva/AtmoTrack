from dataclasses import dataclass

@dataclass
class Weather:
    city: str
    temperature_c: float
    condition: str
    source: str
