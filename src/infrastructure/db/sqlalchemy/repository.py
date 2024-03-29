from typing import List, Optional

from sqlalchemy.orm import Query, Session

from domain.entities.restaurant import Restaurant
from domain.repository import RestaurantRepository


class SQLAlchemyRestaurantRepository(RestaurantRepository):
    """
    Secondary adapter providing ORM SQLAlchemy implementation for :class:`Restaurant`
    instances storage
    """

    def __init__(self, session: Session):
        self.session = session

    @property
    def queryset(self) -> Query:
        return self.session.query(Restaurant)

    def get(self, restaurant_id: int) -> Optional[Restaurant]:
        return self.queryset.get(restaurant_id)

    def all(self) -> List[Restaurant]:
        return self.queryset.all()

    def add(self, restaurant: Restaurant) -> None:
        self.session.add(restaurant)
        self.session.flush()
