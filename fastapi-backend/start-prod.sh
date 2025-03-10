#!/bin/bash

# Activate the virtual environment
source venv/bin/activate
export ENVIRONMENT="production"
export FRONTEND_URL="https://raspi.valgard.org"

# Run the FastAPI application using Uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
