import asyncio
import sys
from logging.config import fileConfig
from pathlib import Path

from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool


BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from app.infrastructure.core import settings
from app.models.dbModels.EntityDB import metadata


config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = metadata
db_url = str(settings.ASYNC_DATABASE_URI)


def run_migrations_offline() -> None:
    """Запуск миграций в оффлайн-режиме.

    В оффлайн-режиме конфигурация выполняется только с URL-адресом,
    и соединение с базой данных не требуется.
    """
    context.configure(
        url=db_url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    """Настройка миграций для онлайн-режима."""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Запуск миграций в онлайн-режиме.

    Создаётся асинхронный движок и выполняется подключение.
    """
    connectable = create_async_engine(
        db_url,
        echo=True,
        future=True,
        poolclass=NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
