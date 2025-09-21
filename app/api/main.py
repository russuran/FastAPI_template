from fastapi import APIRouter

from app.api.routes import ExampleRoute

api_router = APIRouter()

api_router.include_router(ExampleRoute.router, prefix="/example", tags=["example"])
