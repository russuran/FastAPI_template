"""
Пример сервиса, демонстрирующий работу с репозиторием через интерфейс.
Сервисы содержат бизнес-логику приложения и работают с данными через репозитории.
"""

from sqlalchemy.ext.asyncio import AsyncSession
from dependency_injector import providers

from app.infrastructure.interfaces.services.IExampleService import IExampleService
from app.infrastructure.repositories.ExampleRepository import ExampleRepository
from app.infrastructure.schemas.dtoModels.ExampleDTO import ExampleDTO


class ExampleService(IExampleService):
    """
    Пример сервиса, который переворачивает текст.
    Демонстрирует:
    - Внедрение зависимостей через конструктор
    - Использование репозитория через его интерфейс
    - Асинхронную обработку данных
    """
    def __init__(self, example_repository: ExampleRepository):
        self._repository = example_repository

    async def get_text(self, session: AsyncSession, example: ExampleDTO) -> ExampleDTO:
        """
        Получает текст и возвращает его в перевернутом виде.
        
        Args:
            session: Сессия базы данных
            example: DTO с текстом
            
        Returns:
            DTO с перевернутым текстом
        """
        return await self._repository.add_example(session, example)