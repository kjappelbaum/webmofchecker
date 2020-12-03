FROM python:3.8-slim-buster

RUN useradd lsmo

WORKDIR /home/lsmo

COPY requirements.txt .
COPY logging_config.ini .

COPY webmofchecker ./webmofchecker

RUN pip install --no-cache-dir -r requirements.txt