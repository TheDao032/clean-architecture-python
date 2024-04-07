import abc

from sqlalchemy.orm import Session
from internal.domain.entities.dumpuser import DumpUser


class DumpUserCommandRepository(abc.ABC):
    @abc.abstractmethod
    def create_user(self, db: Session, *, obj_in: DumpUser) -> DumpUser:
        pass

    @abc.abstractmethod
    def update_user(self, db: Session, *, obj_in: DumpUser) -> DumpUser:
        pass
