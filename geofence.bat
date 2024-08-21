@echo off

echo Started.
echo %time%
python src\generate.py
python src\data.py
echo %time%