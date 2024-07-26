from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from todo_list_backend_fastapi.schemas import (
    Message,
    TextoHtml,
    UserPublic,
    UserSchema,
)

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get(
    '/hello',
    status_code=HTTPStatus.OK,
    response_class=HTMLResponse,
    response_model=TextoHtml,
)
def say_hello():
    text = """
    <html>
      <head>
        <title>🙂</title>
      </head>
      <body>
        <h1> Hello! </h1>
        <img src="https://http.dog/200.jpg" alt="200 OK" width="300">
      </body>
    </html>"""
    return HTMLResponse(content=text)


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    return user
