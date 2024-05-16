FROM python:3.12-slim as base
WORKDIR /app

COPY ./memory ./memory

FROM base as builder
COPY requirements/prod.txt .
RUN pip install --no-cache-dir -r ./prod.txt

FROM builder as dev
ENV ENV=dev
COPY requirements/dev.txt .
RUN pip install --no-cache-dir -r ./dev.txt
COPY . .

FROM builder as prod
ENV ENV=prod