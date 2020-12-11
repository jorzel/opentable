import json
from typing import List

from nameko.web.handlers import http
from nameko_sqlalchemy import Database
from werkzeug.wrappers import Request, Response

from src.domain.factories import RestaurantFactory
from src.domain.serializers import restaurant_serializer, table_serializer
from src.infrastructure.db.setup import Base
from src.infrastructure.db.repository import SQLAlchemyRestaurantRepository


class BookingService:
    name = "booking_service"

    db = Database(Base)

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
        persons: int = request_params.get("persons")
        repo = SQLAlchemyRestaurantRepository(self.db.session)
        restaurant = repo.get(restaurant_id)
        if not restaurant:
            raise Exception("NotExist")
        table = restaurant.book_table(persons)
        self.db.session.commit()
        return Response(
            f"Restaurant: {restaurant.id} table booked: {table_serializer(table)}"
        )
