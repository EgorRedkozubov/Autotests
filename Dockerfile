FROM python:3.10.0

RUN apt-get update && apt-get install -y \
    unixodbc-dev

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /usr/src/app/tests

ENV PYTHONPATH /usr/src/app

#to be continued
