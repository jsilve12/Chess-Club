FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-alpine3.10

COPY requirements.txt /Chess_Club/requirements.txt
RUN apk update && apk add --no-cache postgresql-dev gcc python3-dev musl-dev
RUN pip3 install -r /Chess_Club/requirements.txt

COPY package.json /Chess_Club/package.json
COPY package-lock.json /Chess_Club/package-lock.json
COPY webpack.config.js /Chess_Club/webpack.config.js
WORKDIR /Chess_Club
RUN apk add --no-cache nodejs npm

COPY . /Chess_Club/
RUN npm install
RUN ./node_modules/.bin/webpack
WORKDIR /
CMD uvicorn Chess_Club.main:app --host 0.0.0.0
