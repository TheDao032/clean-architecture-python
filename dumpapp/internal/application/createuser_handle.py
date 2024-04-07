from database.session import SessionLocal
from loguru import logger

from internal.domain.entities import dumpuser
from internal.infrastructure.persistent.dumpuser import command_repository, query_repository
from sqlalchemy.orm import Session
from datetime import datetime,timezone
import time


def insert_user(db: Session,USERS) -> None:
    query_repo = query_repository.DumpUserQueryRepository()
    cmd_repo = command_repository.DumpUserCommandRepository()
    for user in USERS:
        time_created = {
            "time_index":datetime.now(timezone.utc)
        }
        user.update(time_created)
        user_db_output = query_repo.get_user_by_id(db=db, user_id=user["userId"])
        if user_db_output is None or user_db_output.time_created:
            user_in = dumpuser.DumpUser(
                userId=user["userId"],
                name=user["name"],
                phone=user["phone"],
                time_created=user["time_index"]
            )
        user = cmd_repo.create_user(db=db, obj_in=user_in)


def insert_loop(USERS,stop_condition):
    db = SessionLocal()
    idx_records=0
    while idx_records<=stop_condition:
        insert_user(db,USERS)
        idx_records+=1
        time.sleep(1)
    db.close()

