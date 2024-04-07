#!/bin/bash

# Start server
pip install -r requirements.txt
gunicorn main:app -w 6 -k uvicorn.workers.UvicornWorker
