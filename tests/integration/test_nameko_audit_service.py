from datetime import datetime

from src.domain.events.table import BookedTableEvent


def test_audit_service_can_handle_booked_table_event(audit_service):
    event = BookedTableEvent(1, 1, datetime.now())

    event_names = audit_service.handle_booked_table_event(event.as_dict)

    assert event_names == [event.name]
