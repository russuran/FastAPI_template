from enum import Enum
from typing import Any

from environs import Env
from pydantic import PostgresDsn, field_validator
from pydantic_core.core_schema import FieldValidationInfo
from pydantic_settings import BaseSettings

env = Env()
env.read_env()


class ModeEnum(str, Enum):
    development = "development"
    production = "production"
    testing = "testing"


class Settings(BaseSettings):
    mode: str = ModeEnum.development

    DATABASE_USER: str = env("DATABASE_USER")
    DATABASE_PASSWORD: str = env("DATABASE_PASSWORD")
    DATABASE_HOST: str = env("DATABASE_HOST")
    DATABASE_PORT: int = env("DATABASE_PORT", 5432)
    DATABASE_NAME: str = env("DATABASE_NAME")

    ASYNC_DATABASE_URI: PostgresDsn | None = None

    @field_validator("ASYNC_DATABASE_URI", mode="after")
    def assemble_db_connection(cls, v: str | None, info: FieldValidationInfo) -> Any:
        if not v:
            return PostgresDsn.build(
                scheme="postgresql+asyncpg",
                username=info.data["DATABASE_USER"],
                password=info.data["DATABASE_PASSWORD"],
                host=info.data["DATABASE_HOST"],
                port=info.data["DATABASE_PORT"],
                path=info.data["DATABASE_NAME"],
            )
        return v


settings = Settings()
