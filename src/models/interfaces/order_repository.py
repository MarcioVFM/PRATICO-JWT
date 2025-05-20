from abc import ABC, abstractmethod

class OrdersRepositoryInterface(ABC):

    @abstractmethod
    def register_order(self, description: str, date: str, user_id: int) -> None: pass

    @abstractmethod
    def list_user_orders(self, user_id: int) -> tuple[int, str, str, int]: pass