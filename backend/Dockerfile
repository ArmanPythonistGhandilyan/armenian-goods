FROM python:3.12.1-alpine

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_PASSWORD=admin
ENV DJANGO_SUPERUSER_EMAIL=admin@example.com

WORKDIR /root

COPY ./pyproject.toml ./poetry.lock /root

RUN apk update && \
    apk add --no-cache python3-dev \
    gcc \
    musl-dev \
    libpq-dev

RUN python -m pip install --upgrade pip \
    && pip install --upgrade poetry \
    && poetry config virtualenvs.create false \
    && poetry lock --no-update \
    && poetry install --no-root --no-interaction --no-ansi

COPY . /root 

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]