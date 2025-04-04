.PHONY: test clean

# Run all tests in the project
test:
	python -m unittest discover -s . -p "*_test.py"

# Clean up Python cache files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +

# Default target
all: test 

build-web:
	stickytape game_web.py --add-python-path web --add-python-path data_model --add-python-path coordinators --add-python-path textual --output-file tritium_bundle.py

build-cli:
	stickytape game_cli.py --add-python-path web --add-python-path data_model --add-python-path coordinators --add-python-path textual --output-file tritium_cli.py