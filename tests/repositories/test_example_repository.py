import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.repositories.ExampleRepository import ExampleRepository
from app.infrastructure.schemas.dtoModels.ExampleDTO import ExampleDTO

@pytest.fixture
def example_repository() -> ExampleRepository:
    return ExampleRepository()

@pytest.mark.asyncio
async def test_add_example(example_repository: ExampleRepository, db: AsyncSession):
    # Arrange
    example_dto = ExampleDTO(id=1, text="Hello")
    expected_text = "olleH"  # Reversed "Hello"
    
    # Act
    result = await example_repository.add_example(db, example_dto)
    
    # Assert
    assert result.id == example_dto.id
    assert result.text == expected_text

@pytest.mark.asyncio
async def test_add_example_empty_text(example_repository: ExampleRepository, db: AsyncSession):
    # Arrange
    example_dto = ExampleDTO(id=1, text="")
    
    # Act
    result = await example_repository.add_example(db, example_dto)
    
    # Assert
    assert result.id == example_dto.id
    assert result.text == ""

@pytest.mark.asyncio
async def test_add_example_special_chars(example_repository: ExampleRepository, db: AsyncSession):
    # Arrange
    example_dto = ExampleDTO(id=1, text="Hello! 123 @#$")
    expected_text = "$#@ 321 !olleH"  # Reversed text with special chars
    
    # Act
    result = await example_repository.add_example(db, example_dto)
    
    # Assert
    assert result.id == example_dto.id
    assert result.text == expected_text
