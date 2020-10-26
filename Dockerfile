FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-alpine3.10

COPY requirements.txt /FastAPI/requirements.txt
RUN apk update && apk add --no-cache postgresql-dev gcc python3-dev musl-dev
RUN pip3 install -r /FastAPI/requirements.txt

COPY package.json /FastAPI/package.json
RUN apk add --no-cache nodejs npm
RUN npm install

COPY . /FastAPI/
RUN ./node_modules/.bin/webpack
WORKDIR /
CMD uvicorn FastAPI.main:app
