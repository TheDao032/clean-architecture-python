from database.session import SessionLocal
from loguru import logger

from internal.domain.entities import dumpuser
from internal.infrastructure.persistent.dumpuser import curd_repository, query_repository
from sqlalchemy.orm import Session

ALPHA_USERS = [
    {
    }
]

USERS = [
    {
        "userId": "7",
        "phone": "+84904444777",
        "name": "demo7"
    }
]


def init_db(db: Session) -> None:
    query_repo = query_repository.DumpUserQueryRepository()
    cmd_repo = curd_repository.DumpUserCommandRepository()
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
    while (1):
        logger.info("Inserting row to data")
        init_db(db)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
     main()
