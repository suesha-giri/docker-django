FROM python:3

ENV PYTHONBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requiremnets.txt

RUN pip install -r requirements.txt

COPY . /app


