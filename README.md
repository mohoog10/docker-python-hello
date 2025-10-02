# docker-python-hello

A simple Python app that runs inside Docker.

## ✨ Features
- Prints a greeting with your name (set via environment variable `YOUR_NAME`)
- Shows the current Python version
- Displays the current UTC time

## 🚀 Run locally

```bash
# Build the Docker image
docker build -t hello-docker .

# Run the container with your name
docker run --rm -e YOUR_NAME="Moha" hello-docker
