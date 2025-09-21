import pytest
from unittest.mock import AsyncMock, MagicMock
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.interfaces.repositories.IExampleRepository import IExampleRepository
from app.services.ExampleService import ExampleService
from app.infrastructure.schemas.dtoModels.ExampleDTO import ExampleDTO

class MockExampleRepository(IExampleRepository):
    async def add_example(self, session: AsyncSession, dtoModel: ExampleDTO) -> ExampleDTO:
        return ExampleDTO(id=dtoModel.id, text=dtoModel.text[::-1])

@pytest.fixture
def mock_repository() -> IExampleRepository:
    return MockExampleRepository()

@pytest.fixture
def example_service(mock_repository: IExampleRepository) -> ExampleService:
    return ExampleService(example_repository=mock_repository)

@pytest.mark.asyncio
async def test_get_text(example_service: ExampleService, db: AsyncSession):
    # Arrange
    example_dto = ExampleDTO(id=1, text="Hello")
    expected_text = "olleH"  # Reversed "Hello"
    
    # Act
    result = await example_service.get_text(db, example_dto)
    
    # Assert
    assert result.id == example_dto.id
    assert result.text == expected_text

@pytest.mark.asyncio
async def test_get_text_with_spy():
    # Arrange
    mock_repo = AsyncMock(spec=IExampleRepository)
    mock_repo.add_example.return_value = ExampleDTO(id=1, text="olleH")
    service = ExampleService(example_repository=mock_repo)
    example_dto = ExampleDTO(id=1, text="Hello")
    session = AsyncMock(spec=AsyncSession)
    
    # Act
    result = await service.get_text(session, example_dto)
    
    # Assert
    mock_repo.add_example.assert_called_once_with(session, example_dto)
    assert result.id == example_dto.id
    assert result.text == "olleH"
