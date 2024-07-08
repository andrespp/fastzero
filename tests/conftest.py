import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from fast_zero.app import app
from fast_zero.database import get_session
from fast_zero.models import User, table_registry
from fast_zero.settings import Settings


@pytest.fixture()
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as cli:
        app.dependency_overrides[get_session] = get_session_override
        yield cli

    app.dependency_overrides.clear()


@pytest.fixture()
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    table_registry.metadata.create_all(engine)

    with Session(engine) as s:
        yield s

    table_registry.metadata.drop_all(engine)


@pytest.fixture()
def user(session):
    user = User(
        username='user', email='test_user@example.com', password='password'
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    return user


@pytest.fixture()
def settings():
    return Settings()
