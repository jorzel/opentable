from src.domain.table import Table


def test_can_book_table_should_pass_if_table_is_open_and_has_persons_capacity():
    table = Table(restaurant_id=1, is_open=True, max_persons=4)

    assert table.can_book(3)


def test_can_book_table_should_fail_if_table_is_not_open():
    table = Table(restaurant_id=1, is_open=False, max_persons=4)

    assert not table.can_book(3)


def test_can_book_table_should_fail_if_table_is_open_but_exceed_persons_capacity():
    table = Table(restaurant_id=1, is_open=False, max_persons=4)

    assert not table.can_book(6)
