#!/bin/bash

sleep 10

alembic upgrade head

uvicorn main:main_app --reload --host 0.0.0.0 --port 8008