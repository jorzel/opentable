from dataclasses import asdict
from typing import List

from nameko.events import EventDispatcher

from src.domain.events import DomainEvent
from src.domain.events.publisher import EventPublisher


class NamekoEventPublisher(EventPublisher):
    def __init__(self, dispatcher: EventDispatcher):
        self._dispatcher = dispatcher

    def publish(self, events: List[DomainEvent]) -> None:
        for event in events:
            self._dispatcher(event.name, asdict(event))
