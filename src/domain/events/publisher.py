from abc import ABC, abstractmethod


class EventPublisher(ABC):
    @abstractmethod
    def publish(self, events):
        pass
