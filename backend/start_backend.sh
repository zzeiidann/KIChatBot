#!/bin/bash

# KIChatBot Backend Startup Script
# Uses conda environment for PyTorch compatibility

echo " Starting KIChatBot Backend..."
echo "📦 Activating conda environment: kichatbot"

cd "$(dirname "$0")"
conda run -n kichatbot --no-capture-output --cwd "$(pwd)" python run.py
