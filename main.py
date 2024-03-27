from config.config import settings
from internal.api.http import route
from fastapi import APIRouter, FastAPI

root_router = APIRouter()

app = FastAPI(
    title=settings.API_NAME,
    openurl_api=f"${settings.API_V1_STR}/${settings.API_DOC}"
)


@root_router.get("/ping", status_code=200, tags=["health-check"])
async def health_check():
    return {"message": "pong"}


app.include_router(route.api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)
