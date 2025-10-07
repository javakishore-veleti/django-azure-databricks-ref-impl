from django.conf import settings

from .dummy_event_publisher import DummyEventPublisher
from .kafka_event_publisher import KafkaEventPublisher
from .azure_event_publisher import AzureEventHubPublisher
from .event_publisher_interface import EventPublisher


class EventPublishFactory:
    _cache = {}

    @staticmethod
    def get_event_publisher(event_hub_name: str, reference_id: str) -> EventPublisher:
        """
        Returns an EventPublisher instance based on the environment and event hub name.

        Uses caching based on the reference ID to avoid creating multiple instances.
        Supports multiple Event Hub names and ensures they are consistent between Kafka and Azure.
        """
        cache_key = f"{event_hub_name}_{reference_id}"

        # Check if we have already cached the publisher for this reference_id and event hub name
        if cache_key in EventPublishFactory._cache:
            return EventPublishFactory._cache[cache_key]

        # Check if the event hub name is valid
        if event_hub_name not in settings.EVENT_HUB_NAMES:
            raise ValueError(f"Event Hub '{event_hub_name}' is not in the allowed list of Event Hubs.")

        # Configure the publisher based on the environment variable
        if settings.USE_AZURE:
            # Azure Event Hub publisher
            publisher = AzureEventHubPublisher(
                connection_string=settings.AZURE_EVENT_HUB_CONNECTION_STRING,
                eventhub_name=event_hub_name
            )
        elif settings.USE_KAFKA:
            # Kafka publisher for local development
            publisher = KafkaEventPublisher(
                kafka_bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
                eventhub_name=event_hub_name
            )
        else:
            publisher = DummyEventPublisher(eventhub_name=event_hub_name)



        # Cache the publisher object
        EventPublishFactory._cache[cache_key] = publisher
        return publisher
