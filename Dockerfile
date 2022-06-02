# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/

RUN apt-get update
RUN apt-get -y install python-pip
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt



COPY .. /code/

FROM postgres
ENV POSTGRES_DB support_db
run "createdb" "--template=template0" "support_db"
run  "psql" "-d" "support_db"  --command="create role legenda superuser"
run  "psql" "support_db" "<" "init_data/psql_dump.sql"
COPY psql_dump.sql /docker-entrypoint-initdb.d/

FROM celery
RUN celery -A SupportAPI worker -l info

FROM redis
RUN sudo apt-get install redis-server
RUN sudo service redis-server start
