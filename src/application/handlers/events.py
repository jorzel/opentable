import logging
from typing import Dict, List, Any

from src.domain.events.table import DomainEvent

logger = logging.getLogger(__name__)


def handle_events(
    handlers: Dict[DomainEvent, Any], events: List[Dict[str, Any]]
) -> List[str]:
    handled = []
    for event in events:
        handler = handlers.get(event["name"])
        if not handler:
            logger.info(f"Handler for {event} not found")
            continue
        handled.append(handler(event))
    return handled
