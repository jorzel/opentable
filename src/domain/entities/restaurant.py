from datetime import datetime
from typing import List, Optional

from ..events import DomainEventMixin
from ..events.table import BookedTableEvent
from ..value_objects import RestaurantId
from .table import BookedTableException, Table


class Restaurant(DomainEventMixin):
    def __init__(self, restaurant_id: RestaurantId, tables: List[Table]):
        super().__init__()
        self.id = restaurant_id
        self.tables = sorted(tables, key=lambda table: table.max_persons)

    def _get_open_table(self, persons: int) -> Optional[Table]:
        for table in self.tables:
            if table.can_book(persons):
                return table
        return None

    def has_open_table(self, persons: int) -> bool:
        if self._get_open_table(persons):
            return True
        return False

    def book_table(self, persons: int) -> Optional[Table]:
        table = self._get_open_table(persons)
        if table:
            table.book(persons)
            self._record_event(
                BookedTableEvent(
                    table_id=table.id,
                    restaurant_id=self.id,
                    booked_at=datetime.utcnow(),
                )
            )
            return table
        raise BookedTableException("No open tables in restaurant")
