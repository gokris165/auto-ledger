echo "Starting project setup..."

echo "Creating virtual environment..."
$1 -m venv .venv

if [ -d ".venv/bin" ]; then
    source .venv/bin/activate
elif [ -d ".venv/Scripts" ]; then
    source .venv/Scripts/activate
fi

echo "Installing dependencies..."
pip install -r requirements.txt

echo
echo "Project setup complete!"

