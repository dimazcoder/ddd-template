from typing import Type
from app.domain.events import DomainEvent
from app.infrastructure.events.event_mappers.base_event_mapper import EventMapperBase
from app.infrastructure.adapters.kafka_adapter import KafkaProducer

class EventPublisher:
    def __init__(self):
        self.kafka_producer = KafkaProducer(bootstrap_servers='')

    def publish_event(self, message: dict, topic: str):
        pass

    # def publish_event(self, event: Type[DomainEvent], event_mapper: Type[EventMapperBase], topic: str):
    #     pass
    #     if not issubclass(event_mapper, EventMapperBase):
    #         raise TypeError("event_mapper must be a subclass of EventMapperBase")
    #
    #     event_mapper_instance = event_mapper()
    #     event_dict = event_mapper_instance.map_to_dict(event)
    #     message = {key: str(value) for key, value in event_dict.items()}
    #     self.kafka_producer.send(topic, value=message)
