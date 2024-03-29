from typing import List

from nameko.events import EventDispatcher

from domain.events import DomainEvent
from domain.events.publisher import EventPublisher


class NamekoEventPublisher(EventPublisher):
    """
    Secondary port providing implementation of nameko event dispatcher.
    """

    def __init__(self, dispatcher: EventDispatcher):
        self._dispatcher = dispatcher

    def publish(self, events: List[DomainEvent]) -> None:
        for event in events:
            self._dispatcher(event.name, event.as_dict)
