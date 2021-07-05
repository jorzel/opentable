import logging
from typing import Any, Dict, List

from domain.events.table import DomainEvent

logger = logging.getLogger(__name__)


def handle_events(
    handlers: Dict[DomainEvent, Any], events: List[Dict[str, Any]]
) -> List[str]:
    """
    Primary port defining how incoming events are handled.
    `handlers` - is a key / value store, where key is :attr:`DomainEvent.name` and
                 value is callable defining what action should be made when the event is
                 handled
    `events` - list of serialized events
    """
    handled = []
    for event in events:
        handler = handlers.get(event["name"])
        if not handler:
            logger.info(f"Handler for {event} not found")
            continue
        handled.append(handler(event))
    return handled
