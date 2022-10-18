FROM python:3.9

# install poetry
RUN pip3 install poetry

COPY . ./home
WORKDIR /home

# install runtime dependencies and the app
RUN poetry config virtualenvs.create false && poetry install
