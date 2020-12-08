FROM python:3.8-slim-buster

COPY install_packages.sh .
RUN ./install_packages.sh

RUN useradd lsmo

WORKDIR /home/lsmo

COPY requirements.txt .
COPY logging.ini .

COPY webmofchecker ./webmofchecker

RUN pip install --no-cache-dir -r requirements.txt

CMD gunicorn -b 0.0.0.0:$PORT  webmofchecker.main:server
