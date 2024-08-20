from http import HTTPStatus


def test_read_root_should_return_ok_and_hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'message': 'Olá Mundo!'}


def test_say_hello_should_return_ok_and_hello(client):
    response = client.get('/hello')

    assert response.status_code == HTTPStatus.OK

    expected_html = """
    <html>
      <head>
        <title>🙂</title>
      </head>
      <body>
        <h1> Hello! </h1>
        <img src="https://http.dog/200.jpg" alt="200 OK" width="300">
      </body>
    </html>"""

    assert response.text.strip() == expected_html.strip()


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
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'amanda',
                'email': 'amanda@gmail.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
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


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
