from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):

    @abstractmethod
    def registry_user(self, username: str, password: str) -> None: pass
    
    @abstractmethod
    def find_user_by_username(self, username: int) -> tuple[int, str, str]: pass