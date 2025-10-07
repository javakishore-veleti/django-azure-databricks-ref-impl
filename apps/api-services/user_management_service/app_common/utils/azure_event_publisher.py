from azure.eventhub import EventHubProducerClient, EventData
from .event_publisher_interface import EventPublisher


class AzureEventHubPublisher(EventPublisher):
    def __init__(self, connection_string: str, eventhub_name: str):
        self.producer = EventHubProducerClient.from_connection_string(
            connection_string, eventhub_name=eventhub_name
        )
        self.eventhub_name = eventhub_name

    def publish_event(self, event_type: str, event_data: str):
        event_data = EventData(f'{event_type}:{event_data}')
        event_data_batch = self.producer.create_batch()
        event_data_batch.add(event_data)
        self.producer.send_batch(event_data_batch)
