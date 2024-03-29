from dataclasses import dataclass

from domain.value_objects import RestaurantId


@dataclass(frozen=True)
class Command:
    pass


@dataclass(frozen=True)
class BookTableCommand(Command):
    restaurant_id: RestaurantId
    persons: int
