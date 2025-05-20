from src.models.settings.db_connection_handle import dbconnectionhandler
from src.models.repositories.user_repository import UserRepository
from src.controllers.login_creator import LoginCreator
from src.views.login_creator import LoginCreatorView

def login_creator_composer():
    conn = dbconnectionhandler.get_connection()
    model = UserRepository(conn)
    controller = LoginCreator(model)
    view = LoginCreatorView(controller)

    return view