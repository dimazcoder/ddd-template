from abc import ABC, abstractmethod
from app.domain.models import User

class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User):
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> User:
        pass

