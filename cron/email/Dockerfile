FROM python:3.8-alpine

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY . /app/
RUN gunzip /app/key.txt.gz
RUN ls /app/
CMD python3.8 /app/tournaments.py
