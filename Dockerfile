# syntax=docker/dockerfile:1.7

ARG PYTHON_VERSION=3.11.9

FROM python:${PYTHON_VERSION}-slim-bookworm as backend

ENV VENV_PATH=/opt/venv
ENV PATH="$VENV_PATH/bin:$PATH"

RUN python3 -m venv $VENV_PATH

ENV PIP_CACHE_DIR=/root/.cache/pip
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100

RUN mkdir -p $PIP_CACHE_DIR

WORKDIR /backend

COPY backend/ .
COPY requirements.txt .

RUN mkdir -p $PIP_CACHE_DIR

RUN --mount=type=cache,target=/root/.cache/pip \
    python3 -m pip install --upgrade pip setuptools \
    && python3 -m pip install -r requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip \
    python3 -m pip install --upgrade pip setuptools \
    && python3 -m pip install -r requirements.txt

FROM node:22.4-alpine3.19 AS frontend

WORKDIR /frontend

COPY frontend/package*.json .

RUN --mount=type=cache,target=/root/.npm \
    npm install

COPY frontend/ .

RUN npm run build

FROM python:${PYTHON_VERSION}-slim-bookworm as runner

ARG USER_NAME=appuser
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /app

ENV VENV_PATH=/opt/venv
ENV PATH="$VENV_PATH/bin:$PATH"

COPY --from=backend $VENV_PATH $VENV_PATH
COPY --from=backend /backend ./backend
COPY --from=frontend /frontend/public ./frontend/public

RUN groupadd --gid $USER_GID $USER_NAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USER_NAME \
    && mkdir -p /etc/sudoers.d \
    && echo "$USER_NAME ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$USER_NAME \
    && chmod 0440 /etc/sudoers.d/$USER_NAME

# Standardise on locale, don't generate .pyc, enable tracebacks on seg faults
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

USER ${USER_NAME}

EXPOSE 8000

CMD ["sleep", "infinity"]
# CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
