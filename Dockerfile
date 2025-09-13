# python version
FROM python:3.12-slim

# choosing work directory
WORKDIR /app

# copy requirements.txt
COPY ./requirements.txt /core/requirements.txt

# installing requirements.txt
RUN pip install --no-cache-dir -r /core/requirements.txt

# copying this directory in core docker directory
COPY . /app