from kafka import KafkaProducer
from .event_publisher_interface import EventPublisher


class KafkaEventPublisher(EventPublisher):
    def __init__(self, kafka_bootstrap_servers: str, eventhub_name: str):
        self.producer = KafkaProducer(
            bootstrap_servers=kafka_bootstrap_servers,
            value_serializer=lambda v: str(v).encode('utf-8')
        )
        self.eventhub_name = eventhub_name

    def publish_event(self, event_type: str, user_id: str):
        event_data = {'event_type': event_type, 'user_id': user_id}
        self.producer.send(self.eventhub_name, event_data)
        self.producer.flush()
