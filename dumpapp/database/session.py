from config.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    settings.db.construct_db_uri(),
    pool_pre_ping=bool(settings.db.SQLALCHEMY_POOL_PRE_PING),
    pool_size=settings.db.SQLALCHEMY_POOL_SIZE,
    max_overflow=settings.db.SQLALCHEMY_MAX_OVERFLOW,
    pool_timeout=settings.db.SQLALCHEMY_POOL_TIMEOUT,
    pool_recycle=settings.db.SQLALCHEMY_POOL_RECYCLE,
)

SessionLocal = sessionmaker(
    autocommit=bool(settings.db.SQLALCHEMY_SESSION_AUTOCOMMIT),
    autoflush=bool(settings.db.SQLALCHEMY_SESSION_AUTOFLUSH),
    bind=engine,
)
