from dataclasses import dataclass
from simulator.models.enums import StationType

@dataclass
class Station:
    station_id: str
    name: str
    station_type: StationType
    sequence: int
    cycle_time_minutes: float
    capacity: int = 1