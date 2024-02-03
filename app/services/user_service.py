from app.domain.models import User
from app.domain.use_cases import CreateUserUseCase, GetUserUseCase
from app.infrastructure.events.publishers.event_publisher import EventPublisher
from app.domain.repositories import UserRepository
from app.infrastructure.events.user_events import UserCreatedEvent


class UserService:
    def __init__(self, user_repository: UserRepository, event_publisher: EventPublisher):
        self.user_repository = user_repository
        self.event_publisher = event_publisher

    def create_user(self, username: str, email: str, hashed_password: str) -> User:
        use_case = CreateUserUseCase(self.user_repository)
        user = use_case.handle(username, email, hashed_password)

        user_created_event = UserCreatedEvent(user)
        user_created_event.publish(self.event_publisher, topic='user_created_topic')

        return user

    def get_user_by_id(self, user_id: int) -> User:
        use_case = GetUserUseCase(self.user_repository)
        user = use_case.handle(user_id)

        return user
