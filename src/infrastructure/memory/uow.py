from src.application.uow import UnitOfWork


class FakeUnitOfWork(UnitOfWork):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass
