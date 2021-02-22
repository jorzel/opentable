from src.infrastructure.db.sqlalchemy.orm import run_mappers

from .booking import BookingService  # noqa

run_mappers()
