from typing import List
from internal.domain.entities.dumpuser import DumpUser
from internal.domain.interfaces.dumpuser.query_repository import DumpUserQueryRepository
from sqlalchemy.orm import Session


class DumpUserQueryRepository(DumpUserQueryRepository):
    def get_user_by_id(self, db: Session, *, user_id: str) -> DumpUser | None:
        return db.query(DumpUser).filter(DumpUser.userId == user_id).first()

    def get_user_by_phone(self, db: Session, *, phone: str) -> DumpUser | None:
        return db.query(DumpUser).filter(DumpUser.phone == phone).first()

    def get_users(self, db: Session) -> List[DumpUser] | None:
        return db.query(DumpUser).all()
