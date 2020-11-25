from sqlalchemy import MetaData, create_engine

SQLALCHEMY_DATABASE_URI = "sqlite:///mydb.db"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
metadata = MetaData(bind=engine)

from .orm import Restaurant, Table
