from typing import List, Optional

from .table import Table
from ..events.table import BookedTable


class Restaurant:
    def __init__(self, tables: List[Table]):
        self.tables = tables

    def _get_open_table(self, persons: int) -> Optional[Table]:
        for table in self.tables:
            if table.can_book(persons):
                return table
        return None

    def has_open_table(self, persons: int) -> bool:
        if self._get_open_table(persons):
            return True
        return False

    def book_table(self, persons: int) -> Optional[BookedTable]:
        table = self._get_open_table(persons)
        if table:
            table.book(persons)
            return BookedTable(is_open=False)
        return None
