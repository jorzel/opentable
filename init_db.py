from src.infrastructure.db import metadata

metadata.drop_all()
metadata.create_all()
