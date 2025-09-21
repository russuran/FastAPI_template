"""
Пример FastAPI роута.
Демонстрирует работу с DI, сервисами и DTO.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependency_injector.wiring import inject, Provide
from app.infrastructure.core.depends import Container
from app.infrastructure.db.session import fastapi_get_db
from app.infrastructure.schemas.dtoModels.ExampleDTO import ExampleDTO
from app.services.ExampleService import ExampleService

router = APIRouter()

@router.get("/check", status_code=201, response_model=ExampleDTO)
@inject
async def example(
    session: AsyncSession = Depends(fastapi_get_db),
    example_service: ExampleService = Depends(Provide[Container.example_service])
):
    """
    Пример эндпоинта, который переворачивает текст.
    
    Args:
        session: Сессия БД (внедряется автоматически)
        example_service: Сервис (внедряется через DI контейнер)
        
    Returns:
        DTO с перевернутым текстом
    """
    example = await example_service.get_text(session, ExampleDTO(id=1, text="Example"))
    return example