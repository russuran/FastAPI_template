import asyncio
import os
from typing import AsyncGenerator, Generator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

# Переопределяем путь к лог-файлу для тестов
os.environ["LOG_FILE"] = "test.log"

from app.infrastructure.core.depends import Container
from app.main import app

@pytest.fixture(scope="session")
def event_loop() -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def db() -> AsyncGenerator[AsyncSession, None]:
    # В нашем примере мы не используем реальную базу данных
    # поэтому просто создаем мок сессии
    session = AsyncSession()
    yield session

@pytest.fixture(scope="session")
def container() -> Container:
    container = Container()
    return container

@pytest.fixture(scope="session")
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client