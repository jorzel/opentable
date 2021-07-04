from abc import ABC, abstractmethod


class UnitOfWork(ABC):
    """
    Secondary port (interface) for transaction management (usually, but not only
    database transactions)
    """

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, *args):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass
