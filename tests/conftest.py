import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from todo_list_backend_fastapi.app import app
from todo_list_backend_fastapi.models import table_registry


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    # gerenciamento de contexto (tem live)
    with Session(engine) as session:
        # yield -> define até onde é o setup
        # depois do yield -> desfaz o que foi feito
        yield session

    table_registry.metadata.drop_all(engine)
