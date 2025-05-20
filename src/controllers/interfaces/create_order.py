from abc import ABC, abstractmethod

class CreatorOrderInterface(ABC):
    @abstractmethod
    def create(self, description: str, user_id: int) -> dict: pass