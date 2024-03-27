import logging

from database.session import SessionLocal
from loguru import logger
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed
from sqlalchemy.sql import text

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init() -> None:
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
    except Exception as e:
        logger.error(e)
        raise Exception(f"Error precheck db - {e.__traceback__.tb_frame}")
    finally:
        db.close()


def main() -> None:
    logger.info("Initializing DB service")
    init()
    logger.info("Initializing DB finished")


if __name__ == "__main__":
    main()
