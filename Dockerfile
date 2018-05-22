FROM python:3

WORKDIR /usr/src/app

RUN pip install scrapy scrapy-splash

COPY . .