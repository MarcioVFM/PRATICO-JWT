from src.models.settings.db_connection_handle import dbconnectionhandler
from src.models.repositories.user_repository import UserRepository
from src.controllers.login_creator import LoginCreator
from .http_types.http_request import HttpResquest
from .login_creator import LoginCreatorView
import pytest

@pytest.mark.skip
def test_login_creator_view():
    dbconnectionhandler.connect()
    conn = dbconnectionhandler.get_connection()
    model = UserRepository(conn)
    controller = LoginCreator(model)
    view = LoginCreatorView(controller)
    body = {'username': 'saimon', 'password': 'saimon123'}
    http_request = HttpResquest(body)
    response = view.handle(http_request)
    print(response.body)