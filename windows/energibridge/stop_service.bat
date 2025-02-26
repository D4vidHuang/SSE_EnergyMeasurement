@echo off
set SERVICE_NAME=rapl

echo Stopping service %SERVICE_NAME%...
sc stop %SERVICE_NAME%
if %errorlevel% neq 0 (
    echo Service %SERVICE_NAME% is not running or could not be stopped.
)

echo Deleting service %SERVICE_NAME%...
sc delete %SERVICE_NAME%
if %errorlevel% neq 0 (
    echo Service %SERVICE_NAME% could not be deleted.
)

echo Service %SERVICE_NAME% removed successfully.
pause
