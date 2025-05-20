from .user_register import UserRegister
from src.models.repositories.user_repository import UserRepository
from src.models.settings.db_connection_handle import dbconnectionhandler
import pytest

@pytest.mark.skip
def test_user_register():
    dbconnectionhandler.connect()
    conn = dbconnectionhandler.get_connection()
    user_repository = UserRepository(conn)
    user_register = UserRegister(user_repository)
    username = 'Thiago'
    password = 'senha_criptografada'
    user_register.registry(username, password)