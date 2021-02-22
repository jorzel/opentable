from datetime import datetime

from src.domain.events.table import BookedTableEvent
from src.application.handlers.events import handle_events


def test_handler_handle_booked_table_event():
    event = BookedTableEvent(1, 1, datetime.now())

    event_names = handle_events([event.as_dict])

    assert event_names == [event.name]
