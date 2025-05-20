import pytest  # type: ignore
from src.models.settings.db_connection_handle import dbconnectionhandler
from .user_repository import UserRepository


@pytest.mark.skip
def test_registry_user():
    username = 'marcio'
    password = 123
    dbconnectionhandler.connect()
    conn = dbconnectionhandler.get_connection()
    user_repository = UserRepository(conn)
    user_repository.registry_user(username, password)

@pytest.mark.skip
def test_find_user():
    user_id = 1
    dbconnectionhandler.connect()
    conn = dbconnectionhandler.get_connection()
    user_repository = UserRepository(conn)
    user = user_repository.find_user_by_id(user_id)
    print()
    print(user[1])