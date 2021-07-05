import pytest
from fastapi.testclient import TestClient

from src.infrastructure.db.sqlalchemy.setup import (
    engine,
    session_factory,
    metadata,
    Base,
)
from src.api.fastapi_framework import get_db_session, main


def override_get_db():
    Session = session_factory(engine)
    session = Session()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture(scope="session")
def db_session():
    Session = session_factory(engine)
    yield Session()


@pytest.fixture(scope="session", autouse=True)
def db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield


@pytest.fixture(scope="session")
def fastapi_testclient():
    yield TestClient(main)
