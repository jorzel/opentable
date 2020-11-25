from sqlalchemy import MetaData, create_engine

SQLALCHEMY_DATABASE_URI = "'sqlite:///memory:"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
metadata = MetaData(bind=engine)
