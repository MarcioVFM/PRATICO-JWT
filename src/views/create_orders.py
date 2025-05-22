from src.controllers.create_order import CreateOrder
from src.errors.types.http_bad_request import HttpBadRequestError
from .http_types.http_request import HttpResquest
from .http_types.http_response import HttpResponse

class CreateOrdersView:
    def __init__(self, controller: CreateOrder) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpResquest) -> HttpResponse:
        description = http_request.body.get('description')
        user_id = http_request.params.get('user_id')
        self.__validate_inputs(user_id, description)

        response = self.__controller.create(description, user_id)
        return HttpResponse(body={'data': response}, status_code=200)

    def __validate_inputs(self, user_id: any, description: str) -> None:
        if (
            not description
            or not user_id
            or not isinstance(description, str)
        ): raise HttpBadRequestError('Invalid Input')