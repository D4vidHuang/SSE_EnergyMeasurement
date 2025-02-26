@echo off
set SERVICE_NAME=rapl
set DRIVER_PATH=C:\Users\ymche\energibridge-v0.0.7\LibreHardwareMonitor.sys

echo Creating service %SERVICE_NAME%...
sc query %SERVICE_NAME% >nul 2>&1
if %errorlevel% equ 1060 (
    sc create %SERVICE_NAME% type= kernel binPath= "%DRIVER_PATH%"
) else (
    echo Service %SERVICE_NAME% already exists.
)

echo Starting service %SERVICE_NAME%...
sc start %SERVICE_NAME%
if %errorlevel% neq 0 (
    echo Failed to start service %SERVICE_NAME%.
    exit /b %errorlevel%
)

echo Service %SERVICE_NAME% started successfully.
pause
