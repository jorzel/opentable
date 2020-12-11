from dataclasses import dataclass

from src.domain.value_objects import RestaurantId


@dataclass(frozen=True)
class Command:
    pass


@dataclass(frozen=True)
class BookTable(Command):
    restaurant_id: RestaurantId
    persons: int
