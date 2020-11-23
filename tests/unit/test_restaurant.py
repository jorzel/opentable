from src.domain.entities.table import Table
from src.domain.entities.restaurant import Restaurant


def test_restaurant_has_open_table_should_pass_if_any_table_in_restaurant_is_open_in_desired_capacity():
    open_table = Table(max_persons=5, is_open=True)
    restaurant = Restaurant(tables=[open_table])

    assert restaurant.has_open_table(3)


def test_restaurant_has_open_table_should_failed_if_all_tables_are_occupied():
    occupied_table = Table(max_persons=5, is_open=False)
    restaurant = Restaurant(tables=[occupied_table])

    assert not restaurant.has_open_table(3)


def test_restaurant_has_open_table_should_failed_if_all_tables_with_desired_capacity_are_occupied():
    occupied_table = Table(max_persons=5, is_open=False)
    open_table = Table(max_persons=2, is_open=True)
    restaurant = Restaurant(tables=[occupied_table, open_table])

    assert not restaurant.has_open_table(3)


def test_restaurant_book_table_should_pass_and_return_event_when_table_is_open_and_has_persons_capacity():
    open_table = Table(max_persons=5, is_open=True)
    restaurant = Restaurant(tables=[open_table])

    assert restaurant.book_table(3)