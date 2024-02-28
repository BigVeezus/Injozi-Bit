# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# EXPOSE 5000
ENV FLASK_APP=app.py
ENV ENV_FILE_LOCATION=./.env

CMD ["flask", "run", "--host", "0.0.0.0"]