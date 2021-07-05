from sqlalchemy import Boolean, Column, ForeignKey, Integer
from sqlalchemy import Table as sa_Table
from sqlalchemy.orm import mapper, relationship

from domain.entities.restaurant import Restaurant
from domain.entities.table import Table

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


def run_mappers():
    """
    Provides mapping between db tables and domain models.
    """
    mapper(
        Restaurant,
        restaurant,
        properties={"tables": relationship(Table, backref="restaurant")},
    )
    mapper(Table, table)
