from kafka import KafkaProducer
from pydantic import json


class KafkaPublisher:
    def __init__(self, bootstrap_servers: str):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def publish_event(self, topic: str, event: dict):
        self.producer.send(topic, value=event)
        self.producer.flush()
