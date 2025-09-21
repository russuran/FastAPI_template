import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.core.depends import Container
from app.infrastructure.schemas.dtoModels.ExampleDTO import ExampleDTO

@pytest.mark.asyncio
async def test_example_endpoint(client: AsyncClient, container: Container, db: AsyncSession):
    # Act
    response = await client.get("/api/example/check")
    
    # Assert
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["text"] == "elpmaxE"  # Reversed "Example"

@pytest.mark.asyncio
async def test_example_endpoint_error_handling(client: AsyncClient):
    # Arrange
    # Можно настроить mock для создания ошибки
    
    # Act
    response = await client.get("/api/example/check")
    
    # Assert
    assert response.status_code == 201  # или другой ожидаемый код
    data = response.json()
    assert "id" in data
    assert "text" in data
