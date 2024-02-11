FROM python:3.11-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

RUN mkdir app

WORKDIR /app

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.7.1

RUN pip install "poetry==$POETRY_VERSION"

COPY test.py pyproject.toml poetry.lock README.md ./
# if your project is stored in src, uncomment line below
COPY src ./src
# or this if your file is stored in $PROJECT_NAME, assuming `myproject`
# COPY myproject ./myproject
RUN poetry config virtualenvs.in-project true && \
    poetry install --only=main --no-root

CMD ["python", "test.py"]

#FROM base as final
#
#COPY test.py ./
##COPY --from=builder /app/.venv ./.venv
##COPY --from=builder /app/src .
##COPY docker-entrypoint.sh .
#
#CMD ["python", "test.py"]