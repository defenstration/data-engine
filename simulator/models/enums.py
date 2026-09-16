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