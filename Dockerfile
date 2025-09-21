FROM python:3.12


RUN pip install --upgrade pip poetry

WORKDIR /app

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install --no-root

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]