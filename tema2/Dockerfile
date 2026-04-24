FROM python:3.12-slim

#instalez doar flask (pip) si curl (apt)
RUN pip install --no-cache-dir flask && \
    apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

