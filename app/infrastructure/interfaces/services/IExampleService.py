from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.schemas.dtoModels.ExampleDTO import ExampleDTO


class IExampleService(ABC):
    @abstractmethod
    async def get_text(self, session: AsyncSession, example: ExampleDTO) -> ExampleDTO:
        """
        Получить текст развернутый текст
        """
        pass
