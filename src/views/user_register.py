from src.controllers.interfaces.user_register import UserRegisterInterface
from .http_types.http_request import HttpResquest
from .http_types.http_response import HttpResponse

class UserRegisterView:
    def __init__(self, controller: UserRegisterInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpResquest) -> HttpResponse:
        username = http_request.body.get('username')
        password = http_request.body.get('password')
        self.__validate_inputs(username, password)

        response = self.__controller.registry(username, password)
        return HttpResponse(body={'data': response}, status_code=200)

    def __validate_inputs(seelf, username, password) -> None:
        if (
            not username
            or not password
            or not isinstance(password, str)
            or not isinstance(username, str)
        ): raise Exception('Invalid input')