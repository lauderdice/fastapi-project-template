#!/bin/sh
gunicorn app.main:application --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8887
