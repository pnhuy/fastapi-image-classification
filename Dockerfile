FROM python:3.11
WORKDIR /code
COPY pyproject.toml /code/
RUN pip install poetry
ENV POETRY_VIRTUALENVS_CREATE=false
RUN poetry install
COPY ./imgnet /code/imgnet

