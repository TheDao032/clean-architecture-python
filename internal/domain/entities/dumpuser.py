from .base import Base
from sqlalchemy import Column, String, Boolean, DateTime


class DumpUser(Base):
    userId = Column(String(36), index=True)
    name = Column(String(50), nullable=True)
    phone = Column(String(18), index=True, nullable=False)
    isActivate = Column(Boolean, default=False, nullable=True)
    time_created = Column(DateTime,primary_key=True,nullable=False)