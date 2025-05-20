from src.models.interfaces.order_repository import OrdersRepositoryInterface
from .interfaces.create_order import CreatorOrderInterface
from datetime import datetime

class CreateOrder(CreatorOrderInterface):
    def __init__(self, order_repository: OrdersRepositoryInterface) -> None:
        self.__order_repository = order_repository

    def create(self, description: str, user_id: int) -> dict:
        date = datetime.now()
        isodate = date.isoformat()
        self.__order_repository.register_order(description, isodate, user_id)

        return {
            'Message': 'Order register',
            'Order': description
        }