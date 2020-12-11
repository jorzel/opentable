from abc import ABC


class RestaurantRepository(ABC):
    def get(self, restaurant_id):
        pass

    def all(self):
        pass

    def add(self, restaurant):
        pass
