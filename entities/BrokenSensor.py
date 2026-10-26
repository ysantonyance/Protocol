from typing import final


@final
class BrokenSensor:
    def read_temperature(self) -> float:
        raise RuntimeError('Датчик зламаний')

    def get_sensor_id(self) -> str:
        return 'BROKEN-999'