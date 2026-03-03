@echo off
title FilterGems

if not exist venv\Scripts\activate.bat (
    echo [!] ERROR: venv not found.
    echo Please run: python -m venv venv
    echo Then run: pip install -r requirements.txt
    pause
    exit
)

echo [+] Activating Virtual Environment...
call venv\Scripts\activate.bat

echo [+] Starting FilterGems...
python main.py

echo.
echo Done!
pause
