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

    def process_part(
            self, 
            part: Part,
            arrival_time: datetime,
    ) -> tuple[list[Event], datetime]:
        process_start = arrival_time
        process_end = process_start + timedelta(minutes=self.cycle_time_minutes)

        events = [
            Event(
                part_id=part.part_id,
                station_id=self.station_id,
                event_type=EventType.QUEUE_ENTERED,
                timestamp=arrival_time
            ),
            Event(
                part_id=part.part_id,
                station_id=self.station_id,
                event_type=EventType.PROCESS_STARTED,
                timestamp=process_start
            ),
            Event(
                part_id=part.part_id,
                station_id=self.station_id,
                event_type=EventType.PROCESS_COMPLETED,
                timestamp=process_end
            ),
            Event(
                part_id=part.part_id,
                station_id=self.station_id,
                event_type=EventType.STATION_EXITED,
                timestamp=process_end
            )
        ]

        return events, process_end