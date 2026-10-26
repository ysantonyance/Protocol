from entities.BrokenSensor import BrokenSensor
from entities.FakeAlways25 import FakeAlways25
from entities.SimulatedSensor import SimulatedSensor
from entities.TemperatureSensor import TemperatureSensor
from entities.WeatherAPISensor import WeatherAPISensor


def monitor_room(sensors: list[TemperatureSensor]) -> None:
    for sensor in sensors:
        sensor_id = sensor.get_sensor_id()
        try:
            temp = sensor.read_temperature()
            print(f'[{sensor_id}] Temperature: {temp:.1f} °C')
        except Exception as e:
            print(f'[{sensor_id}] Error: {e}')

sensors = [WeatherAPISensor(), SimulatedSensor(base = 21.5, deviation = 3.0), FakeAlways25(), BrokenSensor()]

monitor_room(sensors)

print(isinstance(WeatherAPISensor(), TemperatureSensor))
print(isinstance({"temp": 22}, TemperatureSensor))