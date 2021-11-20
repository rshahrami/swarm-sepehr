FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /api
WORKDIR /api
COPY . /api

RUN pip install --upgrade pip
RUN pip install -r requirement

CMD [ "python", "kafka-producer.py"]