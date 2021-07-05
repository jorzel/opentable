from .entities.restaurant import Restaurant
from .entities.table import Table


def table_serializer(table: Table):
    return {"id": table.id, "max_persons": table.max_persons, "is_open": table.is_open}


def restaurant_serializer(restaurant: Restaurant):
    return {
        "id": restaurant.id,
        "tables": [table_serializer(t) for t in restaurant.tables],
    }
