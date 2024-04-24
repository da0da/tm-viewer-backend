FROM python:3.10 AS base

RUN apt-get update && apt-get upgrade -y
RUN apt-get install liblzo2-dev

ENV POETRY_HOME=/opt/poetry POETRY_VIRTUALENVS_CREATE=false

RUN python -m venv ${POETRY_HOME}
RUN ${POETRY_HOME}/bin/pip install poetry==${POETRY_VERSION:-1.3}

RUN ln -s ${POETRY_HOME}/bin/poetry /usr/local/bin/poetry
COPY ./poetry.lock ./pyproject.toml /usr/src/app/
WORKDIR /usr/src/app/
COPY . /usr/src/app/

RUN poetry install --only main --no-root --no-interaction
