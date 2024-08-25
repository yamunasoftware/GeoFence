#!/bin/bash

echo "Started."
cd src
python generate.py
python data.py
echo "Duration: $SECONDS seconds"