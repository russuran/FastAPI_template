import logging
import os
import sys

import uvicorn
from environs import Env
from fastapi import APIRouter, FastAPI, HTTPException, Request
from loguru import logger

from app.api.main import api_router
from app.infrastructure.core.depends import Container
from app.infrastructure.exception_handler import global_exception_handler
from app.infrastructure.init_db import init_db

env = Env()
env.read_env()
logging.basicConfig(level=logging.INFO)

logger.remove()
log_file = os.getenv("LOG_FILE", "app.log")
logger.add(log_file, rotation="10 MB", level="INFO")
logger.add(sys.stdout, level="INFO")

main_router = APIRouter()
main_router.include_router(api_router)

app = FastAPI()
app.include_router(main_router, prefix="/api")
app.add_exception_handler(Exception, global_exception_handler)

container = Container()
container.wire(modules=[
    __name__,
    "app.api.routes.ExampleRoute",
    "app.services.ExampleService",
    "app.infrastructure.repositories.ExampleRepository"
])

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTP Exception: {exc.detail} - {exc.status_code}")
    return await global_exception_handler(request, exc)

@app.on_event("startup")
async def on_startup():
    await init_db()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
