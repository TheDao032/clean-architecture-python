from internal.api.http.v1 import (
    dumpuser_handler,
    creatuser_handle
)
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(dumpuser_handler.router, prefix="/users", tags=["users-endpoints"])

api_router.include_router(creatuser_handle.router, prefix="/insert", tags=["users-endpoints"])

