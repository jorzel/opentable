class TablePersonsException(Exception):
    pass


class Table:
    def __init__(self, max_persons: int, is_open: bool = True):
        if max_persons < 0:
            raise TablePersonsException(
                f"Table max_persons attribute must be positive integer, passed instead: {max_persons}"
            )
        self.max_persons = max_persons
        self.is_open = is_open

    def can_book(self, persons: int) -> bool:
        if persons < 0:
            raise TablePersonsException(
                f"Argument persons must be positive integer, passed instead: {persons}"
            )
        if not self.is_open:
            return False
        if persons > self.max_persons:
            return False
        return True
