from sqlalchemy.ext.asyncio import create_async_engine

from app.infrastructure.core.config import settings
from app.models.dbModels.ExampleModel import ExampleModel
from app.models.dbModels.EntityDB import EntityDB

async def init_db():
    engine = create_async_engine(str(settings.ASYNC_DATABASE_URI), echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(EntityDB.metadata.create_all)
    await engine.dispose()
