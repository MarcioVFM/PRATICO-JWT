from src.models.settings.db_connection_handle import dbconnectionhandler
from src.models.repositories.orders_repository import OrdersRepository
from src.controllers.list_orders import ListOrders
from src.views.list_orders import ListOrdersView

def list_orders_composer():
    conn = dbconnectionhandler.get_connection()
    model = OrdersRepository(conn)
    controller = ListOrders(model)
    view = ListOrdersView(controller)

    return view