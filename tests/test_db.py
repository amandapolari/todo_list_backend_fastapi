from sqlalchemy import select

from todo_list_backend_fastapi.models import User


def test_create_user(session):
    # engine = create_engine('sqlite:///database.db')
    # criando um banco de dados em memória:

    # engine = create_engine('sqlite:///:memory:')

    # table_registry.metadata.create_all(engine)

    user = User(
        username='amanda', email='amanda@gmail.com', password='Amanda@123'
    )

    session.add(user)
    session.commit()
    session.refresh(user)
    result = session.scalar(
        select(User).where(User.email == 'amanda@gmail.com')
    )

    assert result.username == 'amanda'
    # assert result.username == 'luan'

    # assert user.id == 1
    # assert user.username == 'amanda'
    # assert user.email == 'amanda@gmail.com'
    # assert user.password == 'Amanda@123'
