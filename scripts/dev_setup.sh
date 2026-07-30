#!/bin/bash

# Create venv:
python3 -m venv .venv --prompt GameOfLife

# Activate venv
source .venv/bin/activate

# Install all requirments
pip install -r requirements.txt