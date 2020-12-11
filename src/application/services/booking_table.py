from src.domain.commands import BookTable
from src.domain.repository import RestaurantRepository
from ..uow import UnitOfWork


class RestaurantNotExist(Exception):
    pass


class BookingTableApplicationService:
    def __init__(
        self, restaurant_repository: RestaurantRepository, unit_of_work: UnitOfWork
    ):
        self._restaurant_repository = restaurant_repository
        self._uow = unit_of_work

    def book_table(self, command: BookTable) -> None:
        restaurant = self._restaurant_repository.get(command.restaurant_id)
        if not restaurant:
            raise RestaurantNotExist

        with self._uow:
            restaurant.book_table(command.persons)
