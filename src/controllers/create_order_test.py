import pytest
from .create_order import CreateOrder
from src.models.settings.db_connection_handle import dbconnectionhandler
from src.models.repositories.orders_repository import OrdersRepository

@pytest.mark.skip
def test_create_order():
    dbconnectionhandler.connect()
    conn = dbconnectionhandler.get_connection()
    repository = OrdersRepository(conn)
    controller = CreateOrder(repository)
    description = 'pizza'
    user_id = 2
    controller.create(description, user_id)