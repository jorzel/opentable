from typing import List, Optional

import pytest

from src.domain.entities.restaurant import Restaurant
from src.domain.entities.table import Table


@pytest.fixture
def table_factory():
    def _table_factory(table_id: int, max_persons: int, is_open: bool = True):
        return Table(table_id, max_persons, is_open)

    yield _table_factory


@pytest.fixture
def restaurant_factory():
    def _restaurant_factory(restaurant_id: int, tables: Optional[List[Table]] = None):
        if not tables:
            tables = []
        return Restaurant(restaurant_id, tables)

    yield _restaurant_factory
