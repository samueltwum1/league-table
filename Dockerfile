FROM python:latest

# install poetry
USER root
RUN pip3 install poetry

COPY . ./home
WORKDIR /home

# install runtime dependencies and the app
RUN poetry config virtualenvs.create false && poetry install
