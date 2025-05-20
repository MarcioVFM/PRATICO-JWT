from src.models.settings.db_connection_handle import dbconnectionhandler
from src.models.repositories.user_repository import UserRepository
from src.controllers.user_register import UserRegister
from src.views.user_register import UserRegisterView

def user_registry_composer():
    conn = dbconnectionhandler.get_connection()
    model = UserRepository(conn)
    controller = UserRegister(model)
    view = UserRegisterView(controller)

    return view