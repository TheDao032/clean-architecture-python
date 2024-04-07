import logging
import sys
import os

from config import logging as lg
from config.logging import InterceptHandler

from pydantic_settings import BaseSettings
from loguru import logger


class DBSettings(BaseSettings):
    POSTGRES_DIALECT: str = "postgresql"
    POSTGRES_SSL_PARAM: str = "sslmode=allow"
    POSTGRES_DATABASE_HOST: str = (
        "localhost:5432"
    )
    POSTGRES_DATABASE_NAME: str = "dumpuser_service"
    POSTGRES_DATABASE_USERNAME: str = "postgres"
    POSTGRES_DATABASE_PASSWORD: str = "postgres"
    SQLALCHEMY_POOL_PRE_PING: int = 1
    SQLALCHEMY_POOL_SIZE: int = 25
    SQLALCHEMY_MAX_OVERFLOW: int = 5
    SQLALCHEMY_POOL_TIMEOUT: int = 45
    SQLALCHEMY_POOL_RECYCLE: int = 3600
    SQLALCHEMY_SESSION_AUTOCOMMIT: int = 0
    SQLALCHEMY_SESSION_AUTOFLUSH: int = 0

    class ConfigDict:
        case_sensitive = True
        env_file = os.path.expanduser('.env')
        env_file_encoding = 'utf-8'
        extra = 'ignore'

    def construct_db_uri(self):
        return f"{self.POSTGRES_DIALECT}://{self.POSTGRES_DATABASE_USERNAME}:{self.POSTGRES_DATABASE_PASSWORD}@{self.POSTGRES_DATABASE_HOST}/{self.POSTGRES_DATABASE_NAME}?{self.POSTGRES_SSL_PARAM}"  # noqa: E501


class LoggingSettings(BaseSettings):
    LOGGING_LEVEL: int = logging.DEBUG
    LOGGERS: tuple = ("uvicorn.asgi", "uvicorn.access", "fastapi")
    LOGGING_ENQUEUE: bool = True
    LOGGING_BACKTRACE: bool = True

    # Prod Only
    # LOGGING_SINK_PROD = "prod.log"
    # LOGGING_ROTATION_PROD = "1 week"
    # LOGGING_RETENTION_PROD = "3 days"
    # LOGGING_COMPRESSION_PROD = "zip"


class Settings(BaseSettings):
    ENV: str = "dev"
    API_NAME: str = "Dump User API"
    API_V1_STR: str = "/v1"
    API_DOC: str = "openapi.json"

    db: DBSettings = DBSettings()
    logging: LoggingSettings = LoggingSettings()

    class ConfigDict:
        case_sensitive = True
        env_file = os.path.expanduser('.env')
        env_file_encoding = 'utf-8'
        extra = 'ignore'


def setup_app_logging(config: Settings) -> None:
    logging.getLogger().handlers = [InterceptHandler()]
    for logger_name in config.logging.LOGGERS:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler(level=config.logging.LOGGING_LEVEL)]

    logger.configure(
        handlers=[
            {
                "sink": sys.stderr,
                "enqueue": config.logging.LOGGING_ENQUEUE,
                "backtrace": config.logging.LOGGING_BACKTRACE,
                "level": config.logging.LOGGING_LEVEL,
                "format": lg.format_record_development,
            },
            # {
            #     "sink": config.logging.LOGGING_SINK_PROD,
            #     "rotation": config.logging.LOGGING_ROTATION_PROD,
            #     "retention": config.logging.LOGGING_RETENTION_PROD,
            #     "compression": config.logging.LOGGING_COMPRESSION_PROD,
            #     "level": config.logging.LOGGING_LEVEL,
            #     "format": lg.format_record_production,
            # },
        ]
    )


settings = Settings()
