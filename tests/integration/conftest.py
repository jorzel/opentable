from unittest.mock import Mock

import pytest
from nameko.testing.services import worker_factory
from sqlalchemy.orm import sessionmaker

from src.entrypoints.nameko import BookingService
from src.infrastructure.db.setup import metadata, engine
from tests.utils import RequestFactory


@pytest.fixture
def request_factory():
    return RequestFactory()


@pytest.fixture(scope="session")
def db_connection():
    metadata.drop_all()
    metadata.create_all()
    connection = engine.connect()

    yield connection

    metadata.drop_all()
    engine.dispose()


@pytest.fixture
def db_session(db_connection):
    transaction = db_connection.begin()
    session = sessionmaker(bind=db_connection)
    session = session()

    yield session

    transaction.rollback()
    session.close()


@pytest.fixture
def booking_service(db_session):
    mock_db = Mock()
    mock_db.session = db_session
    yield worker_factory(BookingService, db=mock_db)


@pytest.fixture
def dbrow_factory():
    def _dbrow_factory(factory, session, **kwargs):
        instance = factory(**kwargs)
        session.add(instance)
        session.flush()
        return instance

    yield _dbrow_factory
