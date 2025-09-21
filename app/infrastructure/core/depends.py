"""
Модуль конфигурации Dependency Injection контейнера.
Здесь определяются все зависимости приложения и их жизненный цикл.
"""

from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.core.config import Settings
from app.services.ExampleService import ExampleService
from app.infrastructure.repositories.ExampleRepository import ExampleRepository

import sys

class Container(containers.DeclarativeContainer):
    """
    Основной контейнер DI.
    Определяет все зависимости приложения и их жизненный цикл.
    """
    # Конфигурация приложения
    config = providers.Configuration()

    # Синглтон для настроек
    settings = providers.Singleton(Settings)

    # Репозитории - используем Singleton, так как они stateless
    example_repository = providers.Singleton(
        ExampleRepository
    )

    # Сервисы - используем Factory для создания новых инстансов
    # с правильно внедренными зависимостями
    example_service = providers.Factory(
        ExampleService,
        example_repository=example_repository
    )


# Создаем экземпляр контейнера и подключаем его к текущему модулю
container = Container()
container.wire(modules=[sys.modules[__name__]])