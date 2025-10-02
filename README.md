# docker-python-hello

A simple Python app that runs inside Docker.

## How it works
- Prints a greeting with your name (set via environment variable `YOUR_NAME`).
- Shows Python version and the current UTC time.

## Run locally

```bash
docker build -t hello-docker .
docker run --rm -e YOUR_NAME="Moha" hello-docker
