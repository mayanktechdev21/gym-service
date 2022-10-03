FROM python:3-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apk update && \
    pip install -r requirements.txt

COPY . /app/

RUN apk add --no-cache bash

RUN ln -sf /bin/bash /bin/sh

CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
