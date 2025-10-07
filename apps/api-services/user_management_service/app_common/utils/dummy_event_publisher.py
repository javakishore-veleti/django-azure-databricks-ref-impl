from kafka import KafkaProducer
from .event_publisher_interface import EventPublisher


class DummyEventPublisher(EventPublisher):
    def __init__(self, eventhub_name: str):
        self.eventhub_name = eventhub_name

    def publish_event(self, event_type: str, user_id: str):
        event_data = {'event_type': event_type, 'user_id': user_id}
