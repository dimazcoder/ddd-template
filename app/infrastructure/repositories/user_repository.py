from typing import Type

from app.domain.repositories import UserRepository as UserRepositoryInterface
from app.domain.models import User
from sqlalchemy.orm import Session

class UserRepository(UserRepositoryInterface):
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: User):
        self.session.add(user)
        self.session.commit()
        return user

    def get_by_id(self, user_id: int) -> Type[User] | None:
        return self.session.query(User).filter(User.id == user_id).first()
