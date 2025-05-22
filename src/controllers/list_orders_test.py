from src.models.settings.db_connection_handle import dbconnectionhandler
from src.models.repositories.orders_repository import OrdersRepository
from .list_orders import ListOrders
import pytest

def test_list_orders():
    dbconnectionhandler.connect()
    conn = dbconnectionhandler.get_connection()
    repository = OrdersRepository(conn)
    controller = ListOrders(repository)
    user_id = 5
    orders = controller.list(user_id)
    print()
    print(orders)