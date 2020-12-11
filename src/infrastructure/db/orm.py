from sqlalchemy import Column, ForeignKey, Table as sa_Table, Integer, Boolean
from sqlalchemy.orm import mapper, relationship

from src.domain.entities.table import Table
from src.domain.entities.restaurant import Restaurant
from .setup import metadata

restaurant = sa_Table(
    "restaurant",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
)


table = sa_Table(
    "table",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("restaurant_id", Integer, ForeignKey("restaurant.id")),
    Column("max_persons", Integer),
    Column("is_open", Boolean),
)

mapper(
    Restaurant,
    restaurant,
    properties={"tables": relationship(Table, backref="restaurant")},
)
mapper(Table, table)