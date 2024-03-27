import abc

from typing import List
from sqlalchemy.orm import Session
from internal.domain.entities.dumpuser import DumpUser


class DumpUserQueryRepository(abc.ABC):
    @abc.abstractmethod
    def get_user_by_id(self, db: Session, *, user_id: str) -> DumpUser:
        pass

    @abc.abstractmethod
    def get_user_by_phone(self, db: Session, *, phone: str) -> DumpUser:
        pass

    @abc.abstractmethod
    def get_users(self, db: Session) -> List[DumpUser]:
        pass
