from http import HTTPStatus

from fastapi.testclient import TestClient

from todo_list_backend_fastapi.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (Organização do teste)

    response = client.get('/')  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Afirmando)

    assert response.json() == {'message': 'Olá Mundo!'}
