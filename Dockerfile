ARG PYTHON_VERSION=3.10.9
FROM python:${PYTHON_VERSION}-buster as build-image

# Update and install dependencies
RUN --mount=type=cache,mode=0777,target=/var/cache/apt \
    apt-get -qq update \
    && apt-get -qq dist-upgrade -y \
    && apt-get -qq install lsb-release git \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -m 700 /root/.ssh; \
    touch -m 600 /root/.ssh/known_hosts; \
    ssh-keyscan github.com > /root/.ssh/known_hosts

# poetry
WORKDIR /srv
RUN pip install poetry==1.5.1
COPY poetry.lock pyproject.toml /srv/
ARG POETRY_DEV=false
RUN --mount=type=ssh,id=default --mount=type=cache,mode=0777,target=/root/.cache/pip \
    poetry export -f requirements.txt -o requirements.txt --without-hashes $(test "$POETRY_DEV" = "true" && echo "--with dev") \
    && python -m venv venv && . venv/bin/activate && pip install -r requirements.txt
# end poetry

FROM python:${PYTHON_VERSION}-slim

COPY --from=build-image /srv/venv/ /srv/venv/

ENV PATH="/srv/venv/bin:$PATH"

# Set working directory to function root directory
WORKDIR /app

# Copy the rest of the working directory contents into the container at /app
COPY src/ .
COPY docker/entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
CMD ["run"]
