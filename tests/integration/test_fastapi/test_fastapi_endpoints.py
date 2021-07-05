from src.infrastructure.db.sqlalchemy.repository import SQLAlchemyRestaurantRepository
from .conftest import override_get_db, main, metadata, db


def test_fastapi_booking_endpoint_book_table_should_pass_when_table_in_restaurant_is_available(
    fastapi_testclient, restaurant_factory, table_factory, db_session
):
    repository = SQLAlchemyRestaurantRepository(db_session)
    table = table_factory(table_id=1, max_persons=5, is_open=True)
    restaurant = restaurant_factory(
        restaurant_id=1, tables=[table], repository=repository
    )
    db_session.commit()
    from src.infrastructure.db.sqlalchemy.orm import Restaurant

    print(db_session.query(Restaurant).all())
    response = fastapi_testclient.post(f"/restaurants/{restaurant.id}")

    data = response.json()
    print(data)
    assert data["restaurant_id"] == restaurant.id
    assert data["is_booked"] is True
    assert not db_session.dirty
    assert table.is_open is False
