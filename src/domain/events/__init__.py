from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class DomainEvent:
    @property
    def name(self):
        return self.__class__.__name__.replace("Event", "")


class DomainEventMixin:
    def __init__(self) -> None:
        self._events: List[DomainEvent] = []

    def _record_event(self, event: DomainEvent) -> None:
        self._events.append(event)

    @property
    def events(self) -> List[DomainEvent]:
        return self._events[:]

    def clear_events(self):
        self._events.clear()
