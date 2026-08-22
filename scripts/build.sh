#!/bin/bash
set -e
IMAGE_NAME="devops-k8s-app"
TAG="${1:-latest}"
docker build -t "$IMAGE_NAME:$TAG" ./app
echo "Docker image built successfully."
