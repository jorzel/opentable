def test_booking_service_book_table_should_pass_when_table_in_restaurant_is_available(
    booking_service, dbrow_factory, restaurant_factory, table_factory, request_factory
):
    session = booking_service.db.session
    request = request_factory(json={"persons": 2})
    table = dbrow_factory(
        table_factory, session, table_id=1, max_persons=5, is_open=True
    )
    restaurant = dbrow_factory(
        restaurant_factory, session, restaurant_id=1, tables=[table]
    )

    booking_service.book_table(request, restaurant.id)

    assert not session.dirty
    assert table.is_open is False
    booking_service.dispatcher.assert_called_once_with(
        "BookedTable", {"is_open": False}
    )
