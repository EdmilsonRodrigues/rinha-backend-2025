#!/bin/bash

set -e

echo "Starting FastAPI application..."
echo "Port configured: $APP_PORT"

exec "$@" --port "$APP_PORT"
