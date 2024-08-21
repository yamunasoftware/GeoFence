#!/bin/bash

echo "Started."
python src/generate.py
python src/data.py
echo "Duration: $SECONDS seconds"