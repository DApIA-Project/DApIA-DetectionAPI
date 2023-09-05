FROM python:3.9-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

RUN pip3 install ./openapi_server/controllers/AircraftClassifier-0.0.1-py3-none-any.whl

EXPOSE 3033

ENTRYPOINT ["python3"]

CMD ["-m", "openapi_server"]