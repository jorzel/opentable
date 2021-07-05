from typing import Any, Dict, Optional

from fastapi import Depends, FastAPI, Request

# from sqlalchemy.orm import Session

from src.application.services.booking_table import BookingTableApplicationService
from src.domain.commands import BookTableCommand
from src.infrastructure.db.sqlalchemy.orm import run_mappers
from src.infrastructure.db.sqlalchemy.setup import session_factory, metadata, engine
from src.infrastructure.db.sqlalchemy.repository import SQLAlchemyRestaurantRepository
from src.infrastructure.db.sqlalchemy.uow import SQLAlchemyUnitOfWork
from src.infrastructure.events.local_publisher import LocalEventPublisher


main = FastAPI()
# run_mappers()


def get_db_session(engine):
    Session = session_factory(engine)
    session = Session()
    try:
        yield session
    finally:
        session.close()


@main.post("/restaurants/{restaurant_id}")
def book_table(
    restaurant_id: str,
    persons: int = 1,
    # session: Session = Depends(get_db_session),
) -> Dict[str, Any]:
    session = next(get_db_session(engine))
    print(SQLAlchemyRestaurantRepository(session).all())
    command = BookTableCommand(restaurant_id=restaurant_id, persons=2)
    booking_table_service = BookingTableApplicationService(
        SQLAlchemyRestaurantRepository(session),
        SQLAlchemyUnitOfWork(session),
        LocalEventPublisher(),
    )
    booking_table_service.book_table(command)
    return {"restaurant_id": restaurant_id, "is_booked": True}


# @app.get("/up")
# def up(self, request: Request) -> str:
#     return "I'm alive"


# @app.get("GET", "/restaurants")
# def restaurants(self) -> Response:
#     repo = SQLAlchemyRestaurantRepository(self.db.session)
#     return Response(json.dumps([restaurant_serializer(r) for r in repo.all()]))