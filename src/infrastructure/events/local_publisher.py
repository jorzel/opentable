from typing import List

from application.handlers.events import handle_events
from domain.events import DomainEvent
from domain.events.publisher import EventPublisher


class LocalEventPublisher(EventPublisher):
    def publish(self, events: List[DomainEvent]) -> None:
        handle_events([e.as_dict for e in events])
