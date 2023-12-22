FROM python:3.7-slim-buster

RUN apt-get update \
    && apt-get install -y libpq-dev gcc

RUN pip3 install --upgrade pip

USER root

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./api /code/api
COPY ./.env /code/.env

RUN pip3 install -r requirements.txt

EXPOSE 8080

ENV LISTEN_PORT = 8080

ENTRYPOINT [ "uvicorn", "api.main:app", "--host=0.0.0.0", "--port=8080", "--workers=4" ]

