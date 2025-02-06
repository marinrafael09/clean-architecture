import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.repositories.users_repository import UsersRepository

db_connection = DBConnectionHandler()
connection = db_connection.get_engine().connect()

@pytest.mark.skip(reason="Sensitive test")
def test_insert_select_user():
    mocked_first_name = 'first'
    mocked_last_name = 'last'
    mocked_age = 18

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)

    registry = users_repository.select_user(mocked_first_name)[0]

    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mocked_age

    sql = f'''
        DELETE FROM users
        WHERE id = {registry.id}
    '''
    response = connection.execute(text(sql))
    connection.commit()
