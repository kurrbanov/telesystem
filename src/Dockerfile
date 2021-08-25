FROM python:3.8
LABEL version="0.2"
LABEL maintainer="kurrbanov"

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install
COPY . ./

CMD poetry run python manage.py makemigrations && \
    poetry run python manage.py migrate && \
    poetry run python manage.py runserver 0.0.0.0:8000
