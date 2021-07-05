from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
metadata = MetaData(bind=engine)
Base = declarative_base(metadata=metadata)


def session_factory(engine) -> Session:
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)


# from .orm import Restaurant, Table
