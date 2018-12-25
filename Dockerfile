# Cube Demo System
FROM python:3

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

RUN apt-get install -y \
    python-dev \
    libssl-dev \
    default-libmysqlclient-dev \
    vim



ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
