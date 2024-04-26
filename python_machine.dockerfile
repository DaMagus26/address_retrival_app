FROM python:3.11.9-slim
LABEL authors="mikhail_ovakimyan"

WORKDIR /project

COPY ./requirements.txt ./setup.py ./README.md /tmp/

RUN python3 -m ensurepip --upgrade && \
    pip install --no-cache-dir pip -U && \
    pip install -r /tmp/requirements.txt && \
    pip install --no-cache-dir -e /tmp
