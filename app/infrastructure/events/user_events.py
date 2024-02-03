from typing import Dict
from app.infrastructure.events.base_event import BaseEvent


class UserCreatedEvent(BaseEvent):
    def map(self) -> Dict[str, str]:
        return {
            "user_id": str(self.event.id),
            "username": self.event.username,
            "email": self.event.email
        }

