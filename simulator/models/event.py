from dataclasses import dataclass, field
from datetime import datetime

from simulator.models.enums import EventType

@dataclass
class Event:
    part_id: str
    station_id: str
    event_type: EventType
    timestamp: datetime = field(default_factory=datetime.now)