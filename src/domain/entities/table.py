from ..value_objects import TableId


class TablePersonsException(Exception):
    pass


class BookedTableException(Exception):
    pass


class Table:
    def __init__(self, table_id: TableId, max_persons: int, is_open: bool = True):
        self.id = table_id
        if max_persons < 0:
            raise TablePersonsException(
                f"Table max_persons attribute must be positive integer, passed instead: {max_persons}"
            )
        self.max_persons = max_persons
        self.is_open = is_open

    def can_book(self, persons: int) -> bool:
        if persons < 0:
            raise TablePersonsException(
                f"{self} can_book argument persons must be positive integer, passed instead: {persons}"
            )
        if not self.is_open:
            return False
        if persons > self.max_persons:
            return False
        return True

    def book(self, persons: int) -> None:
        if self.can_book(persons):
            self.is_open = False
        else:
            raise BookedTableException(
                "{self} cannot be booked, becuase is not open now or is too small"
            )
