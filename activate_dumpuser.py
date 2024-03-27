import asyncio
import sys
import time

from database.session import SessionLocal
from config.config import settings, setup_app_logging

from sqlalchemy.orm import Session
from loguru import logger

from internal.infrastructure.persistent.dumpuser.command_repository import (
    DumpUserCommandRepository as dumpusercommandrepo
)
from internal.infrastructure.persistent.dumpuser.query_repository import (
    DumpUserQueryRepository as dumpuserqueryrepo
)


def precheck_db(db: Session):
    try:
        db.execute('SELECT 1')
    except Exception as e:
        logger.error(e)
        raise Exception(f"Error connecting DB - {e.__traceback__.tb_frame}")


async def scan():
    db = None
    try:
        db: Session = SessionLocal()
        # precheck_db(db)

        queryrepo = dumpuserqueryrepo()
        commandrepo = dumpusercommandrepo()
        dumpuser_out = queryrepo.get_users(db=db)

        logger.info(dumpuser_out)
        if dumpuser_out is not None:
            for dumpuser in dumpuser_out:
                if dumpuser.phone != '':
                    dumpuser.isActivate = True
                    commandrepo.update_user(db=db, obj_in=dumpuser)

        logger.info("...completed scan!!!")
    except Exception as e:
        logger.error(e)
        if db and db.is_active:
            db.rollback()

    finally:
        if db and db.is_active:
            db.close()
            logger.info("closed DB")


if __name__ == "__main__":
    start = time.perf_counter()
    setup_app_logging(config=settings)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(scan())

    end = time.perf_counter()
    print(f"Elapsed run time: {end - start} seconds")

    sys.exit()
