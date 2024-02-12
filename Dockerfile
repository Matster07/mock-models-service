FROM python:3.11-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.7.1

RUN pip install --upgrade pip \
    && pip install "poetry==$POETRY_VERSION"

COPY ["pyproject.toml", "poetry.lock", "README.md", "./"]
COPY .env /app/

RUN poetry config virtualenvs.create true \
    && poetry install --only main

# Production Image
FROM builder as production

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app/

COPY src ./src

EXPOSE 8000

CMD ["poetry", "run", "python", "/app/src/main.py"]