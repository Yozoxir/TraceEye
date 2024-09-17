@echo off
echo Checking Python version...

REM 
python --version 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Installing the latest version...
    goto install_python
) else (
    for /f "tokens=2 delims= " %%a in ('python --version') do set version=%%a
    echo Python version installed: %version%

    REM 
    set required_version=3.12.5

    REM 
    if not "%version%"=="%required_version%" (
        echo Updating Python to version %required_version%...
        goto install_python
    ) else (
        echo Python is up to date.
    )
)

REM 
echo Installing required Python packages...
pip install colorama
pip install pystyle
pip install webbrowser
pip install requests
echo All packages installed.
pause
exit

:install_python
echo Downloading and installing Python %required_version%...
REM 
curl -o python-installer.exe https://www.python.org/ftp/python/%required_version%/python-%required_version%-amd64.exe

REM 
start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1

REM 
python --version
if %errorlevel% neq 0 (
    echo Failed to install Python. Please install it manually.
    pause
    exit /b 1
) else (
    echo Python %required_version% installed successfully.
    goto :eof
)
