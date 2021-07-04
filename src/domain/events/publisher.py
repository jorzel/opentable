from abc import ABC, abstractmethod


class EventPublisher(ABC):
    """
    Secondary port defining interface for event dispatchers
    """

    @abstractmethod
    def publish(self, events):
        pass
