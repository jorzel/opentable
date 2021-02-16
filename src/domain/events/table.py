from dataclasses import dataclass
from datetime import datetime

from ..value_objects import RestaurantId, TableId
from . import DomainEvent


@dataclass
class BookedTableEvent(DomainEvent):
    table_id: TableId
    restaurant_id: RestaurantId
    booked_at: datetime
