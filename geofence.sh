#!/bin/bash

echo "Started."
cd src
python -B generate.py
python -B data.py
echo "Duration: $SECONDS seconds"