#!/bin/bash
gunicorn backend.app:app --bind=0.0.0.0:8000

