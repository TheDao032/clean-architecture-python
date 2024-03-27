#!/bin/bash

# Start server
pip install -r requirements.txt
alembic upgrade head
gunicorn main:app -w 6 -k uvicorn.workers.UvicornWorker
