from sqlalchemy import Column, ForeignKey, Table as sa_Table, Integer, Boolean
from sqlalchemy.orm import mapper, relationship

from .db import metadata
from ..domain.entities.table import Table
from ..domain.entities.restaurant import Restaurant

restaurant = sa_Table(
    "retaurant",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
)


table = sa_Table(
    "table",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("restaurant_id", ForeignKey("restaurant.id")),
    Column("max_persons", Integer),
    Column("is_open", Boolean),
)


def run_mappers():
    mapper(
        Restaurant,
        restaurant,
        properties={"tables": relationship(Table, backref="restaurant")},
    )
    mapper(Table, table)
