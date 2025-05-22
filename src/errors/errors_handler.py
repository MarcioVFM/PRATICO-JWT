from .types.http_bad_request import HttpBadRequestError
from .types.http_not_found import HttpNotFoundError
from .types.http_unauthorized import HttpUnauthorizedError
from src.views.http_types.http_response import HttpResponse

def handle_error(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpUnauthorizedError, HttpBadRequestError, HttpNotFoundError)):
        return HttpResponse(
            body={
                'Errors': [{
                    'title': error.name,
                    'datail': error.message
                }]
            },
            status_code= error.status_code
        )
    
    return HttpResponse(
        body={
            'errors': [{
                'title': 'Server Error',
                'message': str(error)
            }]
        }, 
        status_code= 500
    )