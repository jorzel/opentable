from abc import ABC


class UnitOfWork(ABC):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass
