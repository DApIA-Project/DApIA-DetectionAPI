# DApIA Detection API

## Overview

This server is an API detecting anomalies in a ADS-B message stream.

## Requirements

- [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- [Poetry 1.6.1](https://python-poetry.org/docs/#installation)
- [Docker](https://www.docker.com/get-started/)


## Generate API

```shell
docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v7.0.1 generate -i /local/dapia-detection-api.yaml -g python-flask -o /local --package-name dapia_detection_api
```
### Windows
The command above must be carried out in a Windows Powershell

### Linux
Not yet tested

## File Paths Over 260 Characters and manually install tensorflow 
If you have a Windows Home edition, you will have to edit the Windows Registry to remove the 260 Character Path Limit and you have to manually install tensorflow.
A solution to this problem was found in this GitHub solution :
https://github.com/tensorflow/tensorflow/issues/46934#issuecomment-1104673795


## Install dependencies

```shell
poetry install
```

## Run with Poetry

To run the server, please execute the following from the root directory:

```shell
poetry run python -m dapia_detection_api
```
## Run with Docker

To run the server on a Docker container, please execute the following from the root directory:

Build the image:

```bash
docker build -t dapia-detection-api .
```

Start up a container:

```bash
docker run -p 3033:3033 dapia-detection-api
```

## Use API

You can visualize specification of DApIA Detection API at the following URLs:
- UI API specification: [http://localhost:3033/ui/](http://localhost:3033/ui/)
- OpenAPI definition: [http://localhost:3033/openapi.json](http://localhost:3033/openapi.json)