from typing import List, Optional

from src.domain.entities.restaurant import Restaurant
from src.domain.repository import RestaurantRepository
from src.domain.value_objects import RestaurantId


class MemoryRestaurantRepository(RestaurantRepository):
    def __init__(self):
        self._restaurants = {}

    def get(self, restaurant_id: RestaurantId) -> Optional[Restaurant]:
        return self._restaurants.get(restaurant_id)

    def all(self) -> List[Restaurant]:
        return self._restaurants.values()

    def add(self, restaurant: Restaurant) -> None:
        self._restaurants[restaurant.id] = restaurant
