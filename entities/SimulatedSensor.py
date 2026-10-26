import random
from typing import final


@final
class SimulatedSensor:
    def __init__(self, base:float, deviation:float):
        self.base = base
        self.deviation = deviation

    def read_temperature(self) -> float:
        return self.base + random.uniform(-self.deviation, self.deviation)

    def get_sensor_id(self) -> str:
        return f'Simulated-{self.base}'