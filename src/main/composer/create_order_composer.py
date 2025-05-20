from src.models.settings.db_connection_handle import dbconnectionhandler
from src.models.repositories.orders_repository import OrdersRepository
from src.controllers.create_order import CreateOrder
from src.views.create_orders import CreateOrdersView

def create_orders_composer():
    conn = dbconnectionhandler.get_connection()
    model = OrdersRepository(conn)
    controller = CreateOrder(model)
    view = controller(controller)

    return view