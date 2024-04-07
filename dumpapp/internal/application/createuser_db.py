from database.session import SessionLocal
from loguru import logger

from internal.domain.entities import dumpuser
from internal.infrastructure.persistent.dumpuser import command_repository, query_repository
from sqlalchemy.orm import Session
from datetime import datetime,timezone
import time



USERS = [
    {
        "userId": "1",
        "phone": "+84904444777",
        "name": "demo1"
    }
]


def insert_user(db: Session) -> None:
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


def insert_loop():
    db = SessionLocal()
    while True:
        insert_user(db)
        time.sleep(1)
    
    db.close()
