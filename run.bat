@echo off
setlocal
echo ==========================================
echo    STARTING ATTENDANCE SYSTEM 
echo ==========================================
echo.

if not exist venv (
    echo [ERROR] Virtual environment 'venv' not found!
    echo Please run these commands in your terminal first:
    echo python -m venv venv
    echo .\venv\Scripts\pip install -r requirements.txt
    pause
    exit /b
)

echo [INFO] Using virtual environment...
echo [INFO] Press Ctrl+C to stop the server
echo.

.\venv\Scripts\python.exe app.py

if %ERRORLEVEL% neq 0 (
    echo.
    echo [CRITICAL] The app crashed with error code %ERRORLEVEL%.
    pause
)
echo.
echo Press any key to exit...
pause
endlocal
