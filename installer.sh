#!/bin/bash

if command -v python &> /dev/null; then
	PYTHON_CMD="python"
elif command -v python3 &> /dev/null; then
	PYTHON_CMD="python3"
else
	echo "Python is not installed. Please install Python and try again."
	exit 1
fi

if [ -d "venv" ]; then
	echo "Deleting the old virtual environment..."
	rm -rf venv
fi

echo "Creating a new virtual environment..."
$PYTHON_CMD -m venv venv

echo "Installing dependencies..."
source venv/bin/activate
pip install -r requirements.txt
# deactivate

echo "Creating start.sh..."
echo "#!/bin/bash" > start.sh
echo "source venv/bin/activate" >> start.sh
echo "python main.py" >> start.sh
echo "read -p \"Press any key to continue...\"" >> start.sh

chmod +x start.sh

echo "Completed!"
