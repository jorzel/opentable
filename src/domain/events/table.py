from dataclasses import dataclass

from . import DomainEvent


@dataclass
class BookedTableEvent(DomainEvent):
    is_open: bool
    # TODO add restaurant_id and table_id
