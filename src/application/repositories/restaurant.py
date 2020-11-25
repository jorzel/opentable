from typing import Optional

from sqlalchemy.orm import Session, Query

from infrastructure.orm.restaurant import Restaurant


class SQLAlchemyRestaurantRepository:
    def __init__(self, session: Session):
        self.session = session

    @property
    def queryset(self) -> Query:
        return self.session.query(Restaurant)

    def get(self, restaurant_id: int) -> Optional[Restaurant]:
        return self.queryset.get(restaurant_id)

    def add(self, restaurant: Restaurant) -> None:
        self.session.add(restaurant)
        self.session.flush()
