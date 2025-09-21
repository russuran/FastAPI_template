from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.schemas.dtoModels.ExampleDTO import ExampleDTO

class IExampleRepository(ABC):
    @abstractmethod
    async def add_example(self, session: AsyncSession, dtoModel: ExampleDTO) -> ExampleDTO:
        """Add example and return it with reversed text."""
        pass

    
