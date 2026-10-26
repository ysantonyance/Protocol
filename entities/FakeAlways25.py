from typing import final


@final
class FakeAlways25:
    def read_temperature(self) -> float:
        return 25.0

    def get_sensor_id(self) -> str:
        return 'Fake-25'