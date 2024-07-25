from http import HTTPStatus

from fastapi.testclient import TestClient

from todo_list_backend_fastapi.app import app


def test_read_root_should_return_ok_and_hello_world():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'message': 'Olá Mundo!'}


def test_say_hello_should_return_ok_and_hello():
    client = TestClient(app)

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
