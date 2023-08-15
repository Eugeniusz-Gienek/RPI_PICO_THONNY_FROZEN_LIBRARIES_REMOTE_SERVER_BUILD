@echo off
echo Setting Thonny environment... 
cd /D "%~dp0"
set "curr_path=%~dp0"
set last_char_in_path=%curr_path:~-1%
REM echo Current path: %curr_path%
if %last_char_in_path% NEQ \ (set curr_path=%curr_path%\)
echo Current path: %curr_path%
set PYTHONPATH=%curr_path%reupload_custom_firmware\
cd thonny
echo Starting Thonny...
"C:\Program Files (x86)\Thonny\python.exe" -m thonny
cd ..
echo Thonny terminated.
