from .base import Base
from sqlalchemy import Column, String, Boolean


class DumpUser(Base):
    userId = Column(String(36), primary_key=True, index=True)
    name = Column(String(50), nullable=True)
    phone = Column(String(18), index=True, nullable=False)
    isActivate = Column(Boolean, default=False, nullable=True)
