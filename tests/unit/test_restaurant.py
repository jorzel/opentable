def test_restaurant_has_open_table_should_pass_if_any_table_in_restaurant_is_open_in_desired_capacity(
    restaurant_factory, table_factory
):
    open_table = table_factory(max_persons=5, is_open=True)
    restaurant = restaurant_factory(tables=[open_table])

    assert restaurant.has_open_table(3)


def test_restaurant_has_open_table_should_failed_if_all_tables_are_occupied(
    restaurant_factory, table_factory
):
    occupied_table = table_factory(max_persons=5, is_open=False)
    restaurant = restaurant_factory(tables=[occupied_table])

    assert not restaurant.has_open_table(3)


def test_restaurant_has_open_table_should_failed_if_all_tables_with_desired_capacity_are_occupied(
    restaurant_factory, table_factory
):
    occupied_table = table_factory(max_persons=5, is_open=False)
    open_table = table_factory(max_persons=2, is_open=True)
    restaurant = restaurant_factory(tables=[occupied_table, open_table])

    assert not restaurant.has_open_table(3)


def test_restaurant_book_table_should_pass_and_return_event_when_table_is_open_and_has_persons_capacity(
    restaurant_factory, table_factory
):
    open_table = table_factory(max_persons=5, is_open=True)
    restaurant = restaurant_factory(tables=[open_table])

    table = restaurant.book_table(3)

    assert not table.is_open
