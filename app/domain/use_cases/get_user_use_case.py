from typing import Optional
from app.domain.exceptions import UserNotFoundException
from app.domain.models import User
from app.domain.repositories import UserRepository

class GetUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def handle(self, user_id: int) -> Optional[User]:
        try:
            return self.user_repository.get_by_id(user_id)
        except UserNotFoundException:
            return None
