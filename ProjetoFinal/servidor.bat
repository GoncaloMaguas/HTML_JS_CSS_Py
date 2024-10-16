@echo off
echo Iniciando servidor Flask...
start /B python app.py
timeout /t 2 >nul 2>&1
start "" "http://localhost:5001"
exit
