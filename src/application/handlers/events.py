import logging
from typing import Dict, List

from src.domain.events.table import BookedTableEvent

logger = logging.getLogger(__name__)


def handle_events(events: List[Dict]) -> List[str]:
    handled = []
    for event in events:
        handler = handlers.get(event["name"])
        if not handler:
            logger.info(f"Handler for {event} not found")
            continue
        handled.append(handler(event))
    return handled


def booked_table_handler(event: Dict) -> str:
    logger.info(f"Handling {event}")
    return event["name"]


handlers = {BookedTableEvent.name: booked_table_handler}
