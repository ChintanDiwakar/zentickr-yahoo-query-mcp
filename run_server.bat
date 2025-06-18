@echo off

cd /d %~dp0

call env\Scripts\activate

python run_server.py

pause
