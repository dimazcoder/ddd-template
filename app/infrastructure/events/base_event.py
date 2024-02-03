from typing import Type

from app.domain.events import DomainEvent
from app.infrastructure.events.publishers.event_publisher import EventPublisher


class BaseEvent:
    def __init__(self, event: Type[DomainEvent]):
        self.event = event

    def map(self):
        pass

    def publish(self, publisher: EventPublisher, topic: str):
        message = self.map()
        publisher.publish_event(message, topic)
