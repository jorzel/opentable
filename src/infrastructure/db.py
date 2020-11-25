from sqlalchemy import MetaData, create_engine

SQLALCHEMY_DATABASE_URI = "sqlite://"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
metadata = MetaData(bind=engine)
