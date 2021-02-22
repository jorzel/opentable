from src.infrastructure.db.orm import run_mappers

from .booking import BookingService  # noqa

run_mappers()
