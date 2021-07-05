from typing import List, Optional

import pytest

from domain.entities.restaurant import Restaurant
from domain.entities.table import Table
from domain.repository import RestaurantRepository
from infrastructure.db.memory.repository import MemoryRestaurantRepository


@pytest.fixture
def table_factory():
    def _table_factory(table_id: int, max_persons: int, is_open: bool = True):
        return Table(table_id, max_persons, is_open)

    yield _table_factory


@pytest.fixture
def restaurant_factory():
    def _restaurant_factory(
        restaurant_id: int,
        tables: Optional[List[Table]] = None,
        repository: RestaurantRepository = MemoryRestaurantRepository(),
    ):
        if not tables:
            tables = []

        restaurant = Restaurant(restaurant_id, tables)
        repository.add(restaurant)
        return restaurant

    yield _restaurant_factory
