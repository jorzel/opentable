import json
from typing import List

from nameko.web.handlers import http
from nameko_sqlalchemy import Database
from werkzeug.wrappers import Request, Response

from ..application.repositories.restaurant import SQLAlchemyRestaurantRepository
from ..domain.factories import RestaurantFactory
from ..domain.serializers import restaurant_serializer
from ..infrastructure.db import Base


class HttpService:
    name = "http_service"

    db = Database(Base)

    @http("GET", "/up")
    def up(self, request: Request) -> Response:
        return Response("I'm alive")

    @http("GET", "/restaurants")
    def restaurants(self, request: Request) -> Response:
        repo = SQLAlchemyRestaurantRepository(self.db.session)
        return Response(json.dumps([restaurant_serializer(r) for r in repo.all()]))

    @http("POST", "/restaurant")
    def restaurant(self, request: Request) -> Response:
        request_params = json.loads(request.data)
        tables_specifiation: List[int] = request_params.get("tables_specification", [])
        repo = SQLAlchemyRestaurantRepository(self.db.session)
        restaurant = RestaurantFactory().create(tables_specifiation)
        repo.add(restaurant)
        self.db.session.commit()
        return Response(f"Added restaurant: {restaurant_serializer(restaurant)}")
