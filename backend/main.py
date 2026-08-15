import logging
import asyncio

from fastapi import FastAPI
from contextlib import asynccontextmanager
from api.api import router as api_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def heartbeat(interval: int = 120):
    try:
        while True:
            logger.info("Heartbeat from video streaming app")
            asyncio.sleep(interval)
    except asyncio.CancelledError:
        logger.info("Heartbeat task stopping")

@asynccontextmanager
async def lifespan(app: FastAPI):

    heartbeat_task = asyncio.create_task(heartbeat())

    yield

    heartbeat_task.cancel()


app = FastAPI(lifespan=lifespan)

app.include_router(api_router)

@app.get("/health")
async def get_health():
    return {"message":"video streaming backend running"}



