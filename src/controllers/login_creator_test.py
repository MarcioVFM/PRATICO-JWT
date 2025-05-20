from src.models.settings.db_connection_handle import dbconnectionhandler
from src.models.repositories.user_repository import UserRepository
from .login_creator import LoginCreator
import pytest

@pytest.mark.skip
def test_create_login():
    dbconnectionhandler.connect()
    conn = dbconnectionhandler.get_connection()
    repository = UserRepository(conn)
    login_creator = LoginCreator(repository)
    username = 'Thiago'
    password = 'senha_criptografada'
    user = login_creator.create(username, password)
    print(user)