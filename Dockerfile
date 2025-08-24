FROM python:3.12-slim

WORKDIR /core


COPY ./requirements.txt /core/requirements.txt

RUN pip install --no-cache-dir -r /core/requirements.txt

COPY . /core