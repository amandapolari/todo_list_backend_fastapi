from fastapi import FastAPI

from http import HTTPStatus

from todo_list_backend_fastapi.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}
