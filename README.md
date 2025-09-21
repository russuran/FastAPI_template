# FastAPI Clean Architecture Template

Этот проект представляет собой шаблон для создания FastAPI приложений с использованием принципов Clean Architecture и современных практик разработки.

## Архитектура

Проект следует принципам Clean Architecture и имеет следующую структуру:


### Основные принципы:

1. **Dependency Injection**
   - Использование `dependency-injector` для управления зависимостями
   - Четкое разделение интерфейсов и реализаций
   - Легкое тестирование через подмену зависимостей

2. **Repository Pattern**
   - Абстракция работы с данными
   - Интерфейсы в `interfaces/repositories`
   - Реализации в `repositories/`

3. **Service Layer**
   - Бизнес-логика изолирована в сервисах
   - Сервисы используют репозитории через интерфейсы
   - Чистые функции и явные зависимости

## Быстрый старт

1. **Установка зависимостей**
```bash
poetry install
```

2. **Настройка окружения**
```bash
cp .env.example .env
# Отредактируйте .env под свои нужды
```

3. **Запуск приложения**
```bash
docker-compose -f docker-compose.yaml up --build
```

4. **Запуск тестов**
```bash
poetry run pytest
```

## Использование

### Создание нового эндпоинта

1. Создайте DTO в `app/infrastructure/schemas/dtoModels/`
2. Определите интерфейс репозитория в `app/infrastructure/interfaces/repositories/`
3. Реализуйте репозиторий в `app/infrastructure/repositories/`
4. Создайте сервис в `app/services/`
5. Добавьте роут в `app/api/routes/`
6. Зарегистрируйте зависимости в `app/infrastructure/core/depends.py`

### Пример:

```python
# DTO
class UserDTO(BaseModel):
    id: int
    name: str

# Интерфейс репозитория
class IUserRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: int) -> UserDTO:
        pass

# Сервис
class UserService:
    def __init__(self, user_repository: IUserRepository):
        self._repository = user_repository

    async def get_user(self, id: int) -> UserDTO:
        return await self._repository.get_by_id(id)

# Роут
@router.get("/users/{id}")
async def get_user(
    id: int,
    user_service: UserService = Depends(Provide[Container.user_service])
):
    return await user_service.get_user(id)
```

## Тестирование

Проект использует pytest для тестирования. Тесты организованы по слоям:

```
tests/
├── api/              # Тесты API эндпоинтов
├── services/         # Тесты бизнес-логики
└── repositories/     # Тесты репозиториев
```

### Запуск тестов с отчетом о покрытии:

```bash
poetry run pytest --cov=app --cov-report=html
```

### Примеры тестов:

```python
# Тест репозитория
async def test_repository():
    repo = ExampleRepository()
    result = await repo.get_data()
    assert result is not None

# Тест сервиса с моком
async def test_service():
    mock_repo = AsyncMock(spec=IExampleRepository)
    service = ExampleService(mock_repo)
    await service.process_data()
    mock_repo.save.assert_called_once()
```

## Зависимости

- FastAPI
- SQLAlchemy
- Dependency Injector
- Pytest
- Alembic
- Poetry

## Инструменты разработки

1. **Poetry** - управление зависимостями и виртуальным окружением
2. **Alembic** - миграции базы данных
3. **pytest** - тестирование
4. **coverage** - измерение покрытия кода тестами
5. **black** - форматирование кода
6. **ruff** - линтинг
