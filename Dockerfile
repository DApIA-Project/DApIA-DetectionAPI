FROM python:3.11.5-slim

ENV MODE=""
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100
ENV POETRY_VERSION=1.6.1

RUN pip3 install "poetry==$POETRY_VERSION"

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN poetry config virtualenvs.create false
RUN poetry install $MODE --no-interaction --no-ansi

EXPOSE 3033

ENTRYPOINT ["poetry"]
CMD ["run", "python", "-m", "dapia_detection_api"]