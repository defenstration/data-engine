from dataclasses import dataclass
from datetime import datetime, timedelta

from simulator.models.station import Station
from simulator.models.event import Event
from simulator.models.part import Part
from simulator.models.enums import EventType

@dataclass
class StationRuntime:
    station: Station
    next_available_time: datetime

    def process_part(
                self, 
                part: Part,
                arrival_time: datetime,
        ) -> tuple[list[Event], datetime]:
            
            process_start = max(
                  arrival_time,
                  self.next_available_time
            )


            process_end = process_start + timedelta(minutes=self.station.cycle_time_minutes)
    
            events = [
                Event(
                    part_id=part.part_id,
                    station_id=self.station.station_id,
                    event_type=EventType.QUEUE_ENTERED,
                    timestamp=arrival_time
                ),
                Event(
                    part_id=part.part_id,
                    station_id=self.station.station_id,
                    event_type=EventType.PROCESS_STARTED,
                    timestamp=process_start
                ),
                Event(
                    part_id=part.part_id,
                    station_id=self.station.station_id,
                    event_type=EventType.PROCESS_COMPLETED,
                    timestamp=process_end
                ),
                Event(
                    part_id=part.part_id,
                    station_id=self.station.station_id,
                    event_type=EventType.STATION_EXITED,
                    timestamp=process_end
                )
            ]

            self.next_available_time = process_end

            return events, process_end