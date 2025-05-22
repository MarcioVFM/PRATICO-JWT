from .http_types.http_request import HttpResquest
from .http_types.http_response import HttpResponse
from src.controllers.interfaces.list_orders import ListOrdersIterface

class ListOrdersView:
    def __init__(self, controller: ListOrdersIterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpResquest) -> HttpResponse:
        user_id = http_request.params.get('user_id')
        self.__validate_inputs(user_id)

        response = self.__controller.list(user_id)
        return HttpResponse(body={'data': response}, status_code=200)

    def __validate_inputs(self, user_id: any) -> None:
        if not user_id: raise Exception('Invalid Input')