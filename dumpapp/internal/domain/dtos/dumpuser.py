from pydantic import BaseModel
from typing import Optional


class DumpUserCreate(BaseModel):
    userId: str
    name: str
    phone: str


class DumpUserGet(DumpUserCreate):
    isActivate: bool
    pass


class DumpUserResponse(BaseModel):
    code: int
    message: Optional[str]
    data: Optional[DumpUserGet] = None
