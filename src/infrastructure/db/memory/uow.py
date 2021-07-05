from application.uow import UnitOfWork


class FakeUnitOfWork(UnitOfWork):
    """
    Secondary adapter providing implementation of transaction management when
    transaction is not necessary (or should be omitted).
    """

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass
