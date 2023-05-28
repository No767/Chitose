####################################################################################################
## Builder image
####################################################################################################
FROM python:3.11-slim-bullseye AS builder

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update \
  && apt install -y --no-install-recommends \
  build-essential \
  ca-certificates \
  curl

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN python -m pip install --upgrade pip setuptools
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /Chitose

COPY /pyproject.toml /Chitose
COPY /poetry.lock /Chitose

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --only main \
  && pip wheel --wheel-dir=/Chitose/wheels -r requirements.txt

####################################################################################################
## Final image
####################################################################################################
FROM python:3.11-slim-bullseye

RUN apt update \
  && apt install -y --no-install-recommends \
  tini \
  ca-certificates \
  bash \
  netcat

WORKDIR /Chitose
COPY /chitose /Chitose/
COPY /chitose/api /Chitose/api
COPY /chitose/config /Chitose/config
COPY /chitose/__init__.py /Chitose/__init__.py
COPY /chitose/main.py /Chitose/main.py
COPY /docker/start.sh /Chitose/start.sh
COPY /docker/wait-for-it.sh /Chitose/wait-for-it.sh

COPY --from=builder /Chitose/wheels /Chitose/wheels
COPY --from=builder /Chitose/requirements.txt /Chitose/requirements.txt

RUN pip install --upgrade pip setuptools

RUN adduser --disabled-password --gecos "" chitose \
    && chown -R chitose:chitose /Chitose \
    && chmod +x /Chitose/start.sh

USER chitose

ENV PATH="${PATH}:/home/chitose/.local/bin"

EXPOSE 8000

RUN pip install --user --no-index --find-links=/Chitose/wheels -r requirements.txt

ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["/Chitose/start.sh"]

STOPSIGNAL SIGTERM

LABEL org.opencontainers.image.title="Chitose"
LABEL org.opencontainers.image.description="The backend API for Akari"
LABEL org.opencontainers.image.licenses="GPL-3.0"
LABEL org.opencontainers.image.source="https://github.com/No767/Chitose"



