from enum import Enum

class StationType(Enum):
    RECEIVING = "receiving"
    INSPECTION = "inspection"
    PROCESSING = "processing"
    ASSEMBLY = "assembly"
    PACKAGING = "packaging"
    SHIPPING = "shipping"
    MATERIAL_HANDLING = "material_handling"
    CONTROL = "control"


class StationState(Enum):
    IDLE = "idle"
    BUSY = "busy"
    MAINTENANCE = "maintenance"
    OFFLINE = "offline"
    RUNNING = "running"
    DOWN = "down"
    SETUP = "setup"
    STARVED = "starved"
    BLOCKED = "blocked"

class EventType(Enum):
    QUEUE_ENTERED = "queue_entered"
    PROCESS_STARTED = "process_started"
    PROCESS_COMPLETED = "process_completed"
    INSPECTION_PASSED = "inspection_passed"
    INSPECTION_FAILED = "inspection_failed"
    STATION_ENTERED = "station_entered"
    STATION_EXITED = "station_exited"