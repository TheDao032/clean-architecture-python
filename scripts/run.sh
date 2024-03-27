#!/bin/bash

python -m gunicorn main:app -w 6 -k uvicorn.workers.UvicornWorker
