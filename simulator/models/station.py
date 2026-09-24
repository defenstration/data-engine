from dataclasses import dataclass
from datetime import datetime, timedelta


from simulator.models.enums import StationType, EventType
from simulator.models.event import Event
from simulator.models.part import Part


@dataclass
class Station:
    station_id: str
    name: str
    station_type: StationType
    sequence: int
    cycle_time_minutes: float
    capacity: int = 1

    

        