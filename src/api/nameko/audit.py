from typing import Dict

from nameko.events import event_handler

from src.application.handlers.events import handle_events
from src.infrastructure.events.local_handler import handlers


class AuditService:
    name = "audit_service"

    @event_handler("booking_service", "booked_table")
    def handle_booked_table_event(self, payload: Dict):
        return handle_events(handlers=handlers, events=[payload])
