from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.infrastructure.core import settings

# Создание асинхронного двигателя
async_engine = create_async_engine(
    str(settings.ASYNC_DATABASE_URI),
    echo=True,  # Можно оставить True для отладки
    future=True,
)

# Создание асинхронного sessionmaker
async_session_maker = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    autoflush=False,
)


# Dependency для FastAPI
async def fastapi_get_db():
    async with async_session_maker() as db:
        yield db
