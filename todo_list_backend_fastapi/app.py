from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from todo_list_backend_fastapi.schemas import (
    Message,
    TextoHtml,
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()


database = []


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


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    # breakpoint()

    user_with_id = UserDB(
        # criando o id:
        id=len(database) + 1,
        # **user -> pegando todos os campos de user,
        # chave e valor, desmembrando:
        # .model_dump() -> Convertendo o objeto do pydantic em um dicionário:
        **user.model_dump(),
    )

    # Adicionando os usuários ao db fake:
    database.append(user_with_id)

    return user_with_id


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    # se o id for mair que o tamanho da lista ou um número negativo...
    if user_id > len(database) or user_id < 1:
        # raise -> subir o erro do HTTPException
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    del database[user_id - 1]

    return {'message': 'User deleted'}
