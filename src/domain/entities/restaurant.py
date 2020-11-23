from typing import List

from .table import Table


class Restaurant:
    def __init__(self, tables: List[Table]):
        self.tables = tables

    def has_open_table(self, persons: int) -> bool:
        for table in self.tables:
            if table.can_book(persons):
                return True
        return False
