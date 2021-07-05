from datetime import datetime

from src.application.handlers.events import handle_events
from src.domain.events.table import BookedTableEvent


def test_handler_handle_booked_table_event():
    handlers = {BookedTableEvent.name: lambda x: "success"}
    event = BookedTableEvent(1, 1, datetime.now())

    event_names = handle_events(handlers, [event.as_dict])

    assert event_names == ["success"]
