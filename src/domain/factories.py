from typing import List

from .entities.restaurant import Restaurant
from .entities.table import Table


class RestaurantFactory:
    def create(self, tables_specifiation: List[int]):
        tables = []
        for max_persons in tables_specifiation:
            tables.append(Table(max_persons=max_persons))
        return Restaurant(tables=tables)
