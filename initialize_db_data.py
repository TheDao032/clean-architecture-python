from database.session import SessionLocal
from loguru import logger

from internal.domain.entities import dumpuser
from internal.infrastructure.persistent.dumpuser import command_repository, query_repository
from sqlalchemy.orm import Session

ALPHA_USERS = [
    {
    }
]

USERS = [
    {
        "userId": "1",
        "phone": "+84909999999",
        "name": "demo1"
    },
    {
        "userId": "2",
        "phone": "+84909999998",
        "name": "demo2"
    }
]


def init_db(db: Session) -> None:
    query_repo = query_repository.DumpUserQueryRepository()
    cmd_repo = command_repository.DumpUserCommandRepository()
    for user in USERS:
        user_db_output = query_repo.get_user_by_id(db=db, user_id=user["userId"])
        if user_db_output is None or user_db_output["userId"]:
            user_in = dumpuser.DumpUser(
                userId=user["userId"],
                name=user["name"],
                phone=user["phone"],
            )
            user = cmd_repo.create_user(db=db, obj_in=user_in)


def init() -> None:
    db = SessionLocal()
    init_db(db)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
