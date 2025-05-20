import pytest # type: ignore
from src.models.settings.db_connection_handle import dbconnectionhandler
from .orders_repository import OrdersRepository
from datetime import datetime

@pytest.mark.skip
def test_register_order():
    date = datetime.now()
    format_date = date.isoformat()
    description = 'pizza'
    user_id = 1
    dbconnectionhandler.connect()
    conn = dbconnectionhandler.get_connection()
    order_repository = OrdersRepository(conn)
    order_repository.register_order(description, str(format_date), user_id)

@pytest.mark.skip
def test_list_user_orders():
    user_id = 1
    dbconnectionhandler.connect()
    conn = dbconnectionhandler.get_connection()
    order_repository = OrdersRepository(conn)
    orders_list = order_repository.list_user_orders(user_id)
    print(orders_list)