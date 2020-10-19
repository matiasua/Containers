FROM python:3.8.5-alpine3.12

RUN apk add postgresql-dev postgresql-libs gcc musl-dev

RUN mkdir -p  /flask/backend

WORKDIR /flask/backend
EXPOSE 5000
COPY . /flask/backend

COPY ./requirements.txt /flask/backend/requirements.txt

RUN pip install -r requirements.txt


CMD ["flask", "run", "--host=0.0.0.0"]