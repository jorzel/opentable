from abc import ABC, abstractmethod


class RestaurantRepository(ABC):
    """
    Secondary port defining :class:`Restaurant` storage interface
    """

    @abstractmethod
    def get(self, restaurant_id):
        pass

    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def add(self, restaurant):
        pass
