from internal.domain.entities.dumpuser import DumpUser
from internal.domain.interfaces.dumpuser.command_repository import DumpUserCommandRepository
from sqlalchemy.orm import Session
from datetime import datetime,timezone

class DumpUserCommandRepository(DumpUserCommandRepository):
    def create_user(self, db: Session, *, obj_in: DumpUser) -> DumpUser:
        try:
            # Add a time column to the DumpUser object
            obj_in.time_index = datetime.now(timezone.utc)

            db.add(obj_in)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
        else:
            return obj_in

    def update_user(self, db: Session, *, obj_in: DumpUser) -> DumpUser:
        try:
            # Add a time column to the DumpUser object
            obj_in.time_index = datetime.now()

            db.add(obj_in)
            db.commit()
            db.refresh(obj_in)
        except Exception as e:
            db.rollback()
            raise e
        else:
            return obj_in
