from typing import List

from src.application.handlers.events import handle_events
from src.domain.events import DomainEvent
from src.domain.events.publisher import EventPublisher


class LocalEventPublisher(EventPublisher):
    def publish(self, events: List[DomainEvent]) -> None:
        handle_events([e.as_dict for e in events])
