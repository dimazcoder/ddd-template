from app.domain.models import User
from app.domain.repositories import UserRepository

class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def handle(self, username: str, email: str, hashed_password: str) -> User:
        user = User(username=username, email=email, hashed_password=hashed_password)
        return self.user_repository.create(user)
