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


class FakeUnitOfWork(UnitOfWork):
    pass


class SQLAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session):
        self.session = session

    def __enter__(self):
        return self

    def __exit__(self, *args):
        try:
            self.commit()
        except Exception:
            self.rollback()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
