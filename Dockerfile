FROM python:3.10-slim AS base

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt && \
    pip cache purge && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./api ./api
COPY ./monitoring ./monitoring
COPY ./start.sh .
RUN chmod +x start.sh

EXPOSE 8000

CMD ["./start.sh"]