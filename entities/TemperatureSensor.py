from typing import Protocol, runtime_checkable


@runtime_checkable
class TemperatureSensor(Protocol):
    def read_temperature(self) -> float: ...
    def get_sensor_id(self) -> str: ...