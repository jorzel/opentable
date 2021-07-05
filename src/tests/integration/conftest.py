from unittest.mock import Mock

import pytest
from nameko.testing.services import worker_factory
from sqlalchemy.orm import sessionmaker

from api.nameko import AuditService, BookingService
from infrastructure.db.sqlalchemy.setup import engine, metadata
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
    yield worker_factory(BookingService, db=mock_db, dispatcher=Mock())


@pytest.fixture
def audit_service():
    yield worker_factory(AuditService)
