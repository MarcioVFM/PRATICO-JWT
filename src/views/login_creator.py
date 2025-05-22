from src.controllers.interfaces.login_creator import LoginCreatorInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from .http_types.http_request import HttpResquest
from .http_types.http_response import HttpResponse

class LoginCreatorView:
    def __init__(self, controller: LoginCreatorInterface):
        self.__controller = controller

    def handle(self, http_request: HttpResquest) -> HttpResponse:
        username = http_request.body.get('username')
        password = http_request.body.get('password')
        self.__validate_inputs(username, password)

        response = self.__controller.create(username, password)
        return HttpResponse(body={'data': response}, status_code=201)

    def __validate_inputs(self, username: str, password: str) -> None:
        if (
            not username
            or not password
            or not isinstance(username, str)
            or not isinstance(password,str)
        ): raise HttpBadRequestError('Invalid Input')