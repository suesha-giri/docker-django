FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app1
WORKDIR /app1

COPY requirements.txt /app1/

RUN pip install -r requirements.txt

COPY . /app1/

