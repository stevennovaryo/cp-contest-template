@echo off

set PYTHON_VERSION=3.9.0
set PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe

py --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Python is already installed
) else (
    set /p install_python=Python is not installed. Do you want to install it? (Y/N)
    if /i "%install_python%"=="Y" (
        echo Installing Python...
        powershell -Command "& {$ProgressPreference='SilentlyContinue'; Invoke-WebRequest '%PYTHON_URL%' -OutFile 'python-%PYTHON_VERSION%-amd64.exe'}"
        start /wait python-%PYTHON_VERSION%-amd64.exe /quiet
        del python-%PYTHON_VERSION%-amd64.exe
        echo Python has been installed.
    )
)

py -m pre_commit >nul 2>&1
if %errorlevel% equ 0 (
    echo pre-commit is already installed
) else (
    py -m pip install pre-commit
)

pre-commit install

echo Done.
