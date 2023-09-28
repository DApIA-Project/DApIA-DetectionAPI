# DApIA Detection API

## Overview

This server is an API detecting anomalies in a ADS-B message stream.

## Requirements

- Python 3.11.5
- Poetry 1.6.1

To install the anomaly detection module clone this project : https://github.com/DApIA-Project/Anomaly-Detection.git. \
Follow the 'lib compilation' instructions in the README. You have to build the
file `AircraftClassifier-0.0.1-py3-none-any.whl` with

```
python build.py sdist bdist_wheel
```

Move `AircraftClassifier-0.0.1-py3-none-any.whl` in `/openapi_server/controllers/` of this project.

And do this when you are not using docker

```
pip install dist/AircraftClassifier-0.0.1-py3-none-any.whl
``` 

in `/openapi_server/controllers/`

## Usage

To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m openapi_server
```

and open your browser to here:

```
http://localhost:3033/ui/
```

Your OpenAPI definition lives here:

```
http://localhost:3033/openapi.json
```

To launch the integration tests, use tox:

```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

Build the image:

```bash
docker build -t dapia-detection-api .
```

Start up a container:

```bash
docker run -p 3033:3033 dapia-detection-api
```

