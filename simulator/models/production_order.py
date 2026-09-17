from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class ProductionOrder:
    order_id: str
    part_number: str
    quantity: int
    created_at: datetime = field(default_factory=datetime.now)