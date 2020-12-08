FROM python:3.8-slim-buster

COPY install_packages.sh .
RUN ./install_packages.sh

RUN useradd lsmo

WORKDIR /home/lsmo

COPY requirements.txt .
COPY logging.ini .

COPY webmofchecker ./webmofchecker

RUN pip install --no-cache-dir -r requirements.txt

CMD uvicorn webmofchecker.main:app --host=0.0.0.0 --port=$PORT --workers=$WORKERS --loop="uvloop" --http="httptools" --log-config=logging.ini --limit-concurrency=$CONCURRENCY_LIMIT

