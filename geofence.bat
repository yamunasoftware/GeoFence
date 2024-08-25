@echo off

echo Started.
echo %time%
cd src
python generate.py
python data.py
echo %time%