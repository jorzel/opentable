from datetime import datetime
from dataclasses import dataclass

from . import DomainEvent
from ..value_objects import RestaurantId, TableId


@dataclass
class BookedTableEvent(DomainEvent):
    table_id: TableId
    restaurant_id: RestaurantId
    booked_at: datetime
