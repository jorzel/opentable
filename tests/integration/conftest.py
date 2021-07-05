from unittest.mock import Mock

import pytest
from nameko.testing.services import worker_factory

from src.api.nameko import AuditService, BookingService
from src.infrastructure.db.sqlalchemy.setup import metadata, engine, session_factory
from tests.utils import RequestFactory


@pytest.fixture
def request_factory():
    return RequestFactory()


@pytest.fixture(scope="session")
def db_connection():
    # metadata.drop_all()
    metadata.create_all()
    connection = engine.connect()

    yield connection

    # metadata.drop_all()
    engine.dispose()


@pytest.fixture
def db_session(db_connection):
    transaction = db_connection.begin()
    Session = session_factory(db_connection)
    session = Session()

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


# def override_db_session():
#     Session = session_factory(engine)
#     try:
#         session = Session()
#         yield session
#     finally:
#         session.close()


# @pytest.fixture
# def fastapi_testclient():
#     metadata.drop_all()
#     metadata.create_all()

#     main.dependency_overrides[get_db_session] = override_db_session
#     return TestClient(main)
