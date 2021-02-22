from unittest.mock import ANY

from src.infrastructure.db.sqlalchemy.repository import SQLAlchemyRestaurantRepository


def test_nameko_booking_service_book_table_should_pass_when_table_in_restaurant_is_available(
    booking_service,
    restaurant_factory,
    table_factory,
    request_factory,
    db_session,
):
    request = request_factory(json={"persons": 2})
    repository = SQLAlchemyRestaurantRepository(db_session)
    table = table_factory(table_id=1, max_persons=5, is_open=True)
    restaurant = restaurant_factory(
        restaurant_id=1, tables=[table], repository=repository
    )

    booking_service.book_table(request, restaurant.id)

    assert not db_session.dirty
    assert table.is_open is False
    booking_service.dispatcher.assert_called_once_with(
        "BookedTable",
        {"table_id": table.id, "restaurant_id": restaurant.id, "booked_at": ANY},
    )
