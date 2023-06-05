@echo off
setlocal enabledelayedexpansion

set PYTHON_VERSION=3.9.0
set PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe

echo Checking Python %PYTHON_VERSION:~0,3% installation...
py -%PYTHON_VERSION:~0,3%-64 --version >nul 2>&1
if %errorlevel% equ 0 (
  echo Python %PYTHON_VERSION:~0,3% is already installed.
) else (
  :installpython
  set /p install_python="Python %PYTHON_VERSION:~0,3% is not installed. Do you want to download and install it? (Y/N)"
  if /i !install_python! equ Y (
    echo Downloading Python %PYTHON_VERSION:~0,3% installation...
    powershell -Command "& {$ProgressPreference='SilentlyContinue'; Invoke-WebRequest '%PYTHON_URL%' -OutFile 'python-%PYTHON_VERSION%-amd64.exe'}"
    echo Installing Python %PYTHON_VERSION:~0,3%...
    start /wait python-%PYTHON_VERSION%-amd64.exe /quiet
    del python-%PYTHON_VERSION%-amd64.exe
    echo Python has been installed.
  )
  if /i !install_python! equ N (
    goto installprecommit
  ) 
  goto installpython
)

:installprecommit
py -%PYTHON_VERSION:~0,3%-64 --version >nul 2>&1
if not %errorlevel% equ 0 (
  exit /b 1
)

py -%PYTHON_VERSION:~0,3%-64 -m pre_commit >nul 2>&1
if %errorlevel% equ 0 (
  echo pre-commit is already installed.
) else (
  set /p install_precommit="pre-commit is not installed. Do you want to download and install it? (Y/N)"
  if /i !install_precommit! equ Y (
    echo Downloading and installing pre-commit via pip...
    py -%PYTHON_VERSION:~0,3%-64 -m pip install pre-commit
  )
)

pre-commit install

echo Done.
