from unittest.mock import ANY, Mock

import pytest
from src.application.services.booking_table import BookingTableApplicationService
from src.domain.commands import BookTableCommand
from src.domain.events.table import BookedTableEvent
from src.infrastructure.db.memory.repository import MemoryRestaurantRepository
from src.infrastructure.db.memory.uow import FakeUnitOfWork


@pytest.fixture
def mocked_event_publisher():
    return Mock()


def test_booking_service_book_table_should_pass_when_table_in_restaurant_is_available(
    restaurant_factory,
    table_factory,
    mocked_event_publisher,
):
    repository = MemoryRestaurantRepository()
    booking_service = BookingTableApplicationService(
        repository, FakeUnitOfWork(), mocked_event_publisher
    )
    table = table_factory(table_id=1, max_persons=5, is_open=True)
    restaurant = restaurant_factory(
        restaurant_id=1, tables=[table], repository=repository
    )
    command = BookTableCommand(restaurant.id, persons=2)

    booking_service.book_table(command)

    assert table.is_open is False
    mocked_event_publisher.publish.assert_called_once_with(
        [
            BookedTableEvent(
                table_id=table.id, restaurant_id=restaurant.id, booked_at=ANY
            )
        ]
    )
