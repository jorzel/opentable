import json

from nameko.events import EventDispatcher
from nameko.web.handlers import http
from nameko_sqlalchemy import Database
from werkzeug.wrappers import Request, Response

from application.services.booking_table import BookingTableApplicationService
from domain.commands import BookTableCommand
from domain.serializers import restaurant_serializer
from infrastructure.db.sqlalchemy.repository import SQLAlchemyRestaurantRepository
from infrastructure.db.sqlalchemy.setup import Base
from infrastructure.db.sqlalchemy.uow import SQLAlchemyUnitOfWork
from infrastructure.events.nameko_publisher import NamekoEventPublisher


class BookingService:
    name = "booking_service"

    db = Database(Base)
    dispatcher = EventDispatcher()

    @http("POST", "/restaurants/<int:restaurant_id>")
    def book_table(self, request: Request, restaurant_id: int) -> Response:
        request_params = json.loads(request.data)
        command = BookTableCommand(
            restaurant_id=restaurant_id, persons=request_params["persons"]
        )
        booking_table_service = BookingTableApplicationService(
            SQLAlchemyRestaurantRepository(self.db.session),
            SQLAlchemyUnitOfWork(self.db.session),
            NamekoEventPublisher(self.dispatcher),
        )
        booking_table_service.book_table(command)
        return Response(f"Restaurant: {restaurant_id} table booked")

    @http("GET", "/up")
    def up(self, request: Request) -> Response:
        return Response("I'm alive")

    @http("GET", "/restaurants")
    def restaurants(self, request: Request) -> Response:
        repo = SQLAlchemyRestaurantRepository(self.db.session)
        return Response(json.dumps([restaurant_serializer(r) for r in repo.all()]))
