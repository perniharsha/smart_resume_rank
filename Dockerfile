FROM python:3.10-slim AS base

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app
COPY .model ./model
COPY start.sh .

EXPOSE 8000
ENTRYPOINT ["BASH","start.sh"]