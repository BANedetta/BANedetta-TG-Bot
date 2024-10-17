@echo off
if exist venv (
	echo Deleting the old virtual environment...
	rmdir /S /Q venv
)

echo Creating a new virtual environment...
python -m venv venv

echo Installing dependencies...
call venv\Scripts\activate
pip install -r requirements.txt
REM deactivate

echo Creating start.cmd...
echo @echo off > start.cmd
echo call venv\Scripts\activate >> start.cmd
echo python main.py >> start.cmd
echo pause >> start.cmd

echo Completed!
pause