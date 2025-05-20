from abc import ABC, abstractmethod

class ListOrdersIterface(ABC):
    @abstractmethod
    def list(self, user_id: int) -> dict: pass