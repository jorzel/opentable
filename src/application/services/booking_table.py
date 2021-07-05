from src.application.uow import UnitOfWork
from src.domain.commands import BookTableCommand
from src.domain.events.publisher import EventPublisher
from src.domain.repository import RestaurantRepository


class RestaurantNotExist(Exception):
    pass


class BookingTableApplicationService:
    """
    Primary port (use case) defining how incoming requests can book table
    providing `command`
    """

    def __init__(
        self,
        restaurant_repository: RestaurantRepository,
        unit_of_work: UnitOfWork,
        event_publisher: EventPublisher,
    ):
        self._restaurant_repository = restaurant_repository
        self._uow = unit_of_work
        self._event_publisher = event_publisher

    def book_table(self, command: BookTableCommand) -> None:
        restaurant = self._restaurant_repository.get(command.restaurant_id)
        if not restaurant:
            raise RestaurantNotExist

        with self._uow:
            restaurant.book_table(command.persons)
        self._event_publisher.publish(restaurant.events)
        restaurant.clear_events()
