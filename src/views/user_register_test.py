from src.controllers.user_register import UserRegister
from src.models.repositories.user_repository import UserRepository
from src.models.settings.db_connection_handle import dbconnectionhandler
from .user_register import UserRegisterView
from .http_types.http_request import HttpResquest
import pytest

@pytest.mark.skip
def test_user_register():
    dbconnectionhandler.connect()
    conn = dbconnectionhandler.get_connection()
    repository = UserRepository(conn)
    controller = UserRegister(repository)
    view = UserRegisterView(controller)
    body = {'username': 'saimon', 'password': 'saimon123'}
    http_request = HttpResquest(body)
    view.handler(http_request)
    print(view)