from dataclasses import dataclass, asdict
from typing import Dict, List


@dataclass(frozen=True)
class DomainEvent:
    name = ""

    @property
    def as_dict(self) -> Dict:
        serialized = asdict(self)
        serialized["name"] = self.name
        return serialized


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
