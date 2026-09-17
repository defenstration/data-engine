from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Part:
    part_id: str
    part_number: str
    order_id: str
    created_at: datetime = field(default_factory=datetime.now)
