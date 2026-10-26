import json
import urllib.request
from typing import final


@final
class WeatherAPISensor:
    def read_temperature(self) -> float:
        url = 'https://api.open-meteo.com/v1/forecast?latitude=46.48&longitude=30.73&current=temperature_2m'
        try:
            with urllib.request.urlopen(url, timeout=5) as response:
                data = json.loads(response.read().decode())
                return float(data['current']['temperature_2m'])
        except Exception as e:
            raise RuntimeError(f'Couldn\'t get weather info: {e}')

    def get_sensor_id(self) -> str:
        return 'WAS26-Odesa'