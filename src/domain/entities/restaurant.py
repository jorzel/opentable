from typing import List, Optional

from .table import Table


class Restaurant:
    def __init__(self, id: int, tables: List[Table]):
        self.id = id
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
            return table
        return None
