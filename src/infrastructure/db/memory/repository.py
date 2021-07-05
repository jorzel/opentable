from typing import List, Optional

from domain.entities.restaurant import Restaurant
from domain.repository import RestaurantRepository
from domain.value_objects import RestaurantId


class MemoryRestaurantRepository(RestaurantRepository):
    """
    Secondary adapter providing in-memory implementation for :class:`Restaurant`
    instances storage
    """

    def __init__(self):
        self._restaurants = {}

    def get(self, restaurant_id: RestaurantId) -> Optional[Restaurant]:
        return self._restaurants.get(restaurant_id)

    def all(self) -> List[Restaurant]:
        return self._restaurants.values()

    def add(self, restaurant: Restaurant) -> None:
        self._restaurants[restaurant.id] = restaurant
