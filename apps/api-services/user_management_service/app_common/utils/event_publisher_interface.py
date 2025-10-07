from abc import ABC, abstractmethod


class EventPublisher(ABC):
    @abstractmethod
    def publish_event(self, event_type: str, event_data: str):
        pass
