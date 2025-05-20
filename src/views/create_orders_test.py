from src.models.settings.db_connection_handle import dbconnectionhandler
from src.models.repositories.orders_repository import OrdersRepository
from src.controllers.create_order import CreateOrder
from .create_orders import CreateOrdersView
from .http_types.http_request import HttpResquest
import pytest

def test_creat_order():
    dbconnectionhandler.connect()
    conn = dbconnectionhandler.get_connection()
    repository = OrdersRepository(conn)
    controller = CreateOrder(repository)
    view = CreateOrdersView(controller)

    http_request = HttpResquest(body={'description': 'frango'}, params={'user_id': 4})
    response = view.handle(http_request)
    print(response.body)