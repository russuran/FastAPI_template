"""
Пример реализации репозитория.
Репозитории отвечают за работу с данными и изолируют бизнес-логику от деталей хранения.
"""

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.interfaces.repositories.IExampleRepository import IExampleRepository
from app.infrastructure.schemas.dtoModels.ExampleDTO import ExampleDTO


class ExampleRepository(IExampleRepository):
    """
    Пример репозитория, который работает с текстовыми данными.
    В реальном приложении здесь была бы работа с базой данных.
    """
    
    async def add_example(self, session: AsyncSession, dtoModel: ExampleDTO) -> ExampleDTO:
        """
        Сохраняет пример и возвращает его с перевернутым текстом.
        
        Args:
            session: Сессия базы данных
            dtoModel: DTO с данными для сохранения
            
        Returns:
            DTO с перевернутым текстом
        """
        # В реальном приложении здесь был бы код для сохранения в БД
        return ExampleDTO(id=dtoModel.id, text=dtoModel.text[::-1])