#!/bin/bash

# Ensure packages are installed
pip install -r requirements.txt

# Start the app using Gunicorn
gunicorn backend.app:app --bind=0.0.0.0:8000
