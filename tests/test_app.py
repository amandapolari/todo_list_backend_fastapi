from http import HTTPStatus

from todo_list_backend_fastapi.schemas import UserPublic


def test_read_root_should_return_ok_and_hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'amanda',
            'email': 'amanda@gmail.com',
            'password': 'amanda123',
        },
    )

    # Verificando se voltou o status code correto com os dados acima
    assert response.status_code == HTTPStatus.CREATED

    # Verificando se o que volta para o usuário é o UserPublic
    assert response.json() == {
        'username': 'amanda',
        'email': 'amanda@gmail.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    # Schema.model_validate(obj):
    # O código faz a conversão de qualquer objeto para um modelo do pydantic.
    # No caso, está convertendo um objeto 'user' (conftest.py)
    # em um modelo do pydantic 'UserPublic' (schemas.py)
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user(client, user):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
