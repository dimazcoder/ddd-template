from fastapi import Depends
from app.infrastructure.repositories.user_repository import UserRepository
from app.infrastructure.events.publishers.event_publisher import EventPublisher
from app.infrastructure.adapters.mysql_adapter import get_db
from app.services.user_service import UserService
from sqlalchemy.orm import Session

def get_user_service(session: Session = Depends(get_db)) -> UserService:
    user_repository = UserRepository(session)
    event_publisher = EventPublisher()
    return UserService(user_repository, event_publisher)

