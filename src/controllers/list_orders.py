from src.models.interfaces.order_repository import OrdersRepositoryInterface
from .interfaces.list_orders import ListOrdersIterface
from datetime import datetime

class ListOrders(ListOrdersIterface):
    def __init__(self, order_reposoitory: OrdersRepositoryInterface) -> None:
        self.__order_repository = order_reposoitory

    def list(self, user_id: int) -> dict:
        orders = self.__order_repository.list_user_orders(user_id)
        dict_orders = self.__format_response(orders)
        return dict_orders

    def __format_response(self, orders):
        dict_orders = []
        for order in orders:
            order_name = order[1]
            order_date = order[2]
            date_formatted = self.__format_datetime(order_date)

            dict_orders.append({
                'order': order_name,
                'date': date_formatted
            })

        return dict_orders
    
    def __format_datetime(self, order_date: str) -> str:
            order_datetime = datetime.fromisoformat(order_date)
            date_formatted = order_datetime.strftime("%d/%m/%Y %H:%M:%S")
            return date_formatted