from config.config import settings
from internal.api.http import route
from fastapi import APIRouter, FastAPI, BackgroundTasks
from internal.application import createuser_db
import threading
root_router = APIRouter()

def background_job():
    createuser_db.insert_loop()

app = FastAPI(
    title=settings.API_NAME,
    openurl_api=f"${settings.API_V1_STR}/${settings.API_DOC}"
)

@root_router.get("/ping", status_code=200, tags=["health-check","background-insert"])
async def health_check():
    return {"message": "pong"}
async def init(background_tasks: BackgroundTasks):
    background_tasks.add_task(background_job)

app.include_router(route.api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)
