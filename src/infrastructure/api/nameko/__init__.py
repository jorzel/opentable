from src.infrastructure.db.sqlalchemy.orm import run_mappers

from .audit import AuditService  # noqa
from .booking import BookingService  # noqa

run_mappers()
