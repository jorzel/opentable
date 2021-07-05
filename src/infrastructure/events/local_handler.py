import logging
from typing import Any, Dict

from src.domain.events.table import BookedTableEvent

logger = logging.getLogger(__name__)


def booked_table_handler(event: Dict[str, Any]) -> str:
    logger.info(f"Handling {event}")
    # you do here something with event
    return event["name"]


handlers = {BookedTableEvent.name: booked_table_handler}
