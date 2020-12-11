import json
from typing import List

from nameko.events import EventDispatcher
from nameko.web.handlers import http
from nameko_sqlalchemy import Database
from werkzeug.wrappers import Request, Response

from src.application.services.booking_table import BookingTableApplicationService
from src.application.uow import SQLAlchemyUnitOfWork
from src.domain.commands import BookTable
from src.domain.factories import RestaurantFactory
from src.domain.serializers import restaurant_serializer
from src.infrastructure.db.setup import Base
from src.infrastructure.db.repository import SQLAlchemyRestaurantRepository
from src.infrastructure.events.nameko_publisher import NamekoEventPublisher


class BookingService:
    name = "booking_service"

    db = Database(Base)
    dispatcher = EventDispatcher()

    @http("GET", "/up")
    def up(self, request: Request) -> Response:
        return Response("I'm alive")

    @http("GET", "/restaurants")
    def restaurants(self, request: Request) -> Response:
        repo = SQLAlchemyRestaurantRepository(self.db.session)
        return Response(json.dumps([restaurant_serializer(r) for r in repo.all()]))

    @http("POST", "/restaurants")
    def restaurant(self, request: Request) -> Response:
        request_params = json.loads(request.data)
        tables_specifiation: List[int] = request_params.get("tables_specification", [])
        repo = SQLAlchemyRestaurantRepository(self.db.session)
        restaurant = RestaurantFactory().create(tables_specifiation)
        repo.add(restaurant)
        self.db.session.commit()
        return Response(f"Added restaurant: {restaurant_serializer(restaurant)}")

    @http("POST", "/restaurants/<int:restaurant_id>")
    def book_table(self, request: Request, restaurant_id: int) -> Response:
        request_params = json.loads(request.data)
        command = BookTable(
            restaurant_id=restaurant_id, persons=request_params["persons"]
        )
        booking_table_service = BookingTableApplicationService(
            SQLAlchemyRestaurantRepository(self.db.session),
            SQLAlchemyUnitOfWork(self.db.session),
            NamekoEventPublisher(self.dispatcher),
        )
        booking_table_service.book_table(command)
        return Response(f"Restaurant: {restaurant_id} table booked")
