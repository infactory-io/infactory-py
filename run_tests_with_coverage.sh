#!/bin/bash

set -e

# Time the script
START_TIME=$(date +%s)

# Run tests with coverage
poetry run coverage run -m pytest
END_TIME=$(date +%s)

# Calculate and print the duration
DURATION=$((END_TIME - START_TIME))
echo "Tests completed in $DURATION seconds"

# Generate coverage report
poetry run coverage report -m

# Generate HTML coverage report
poetry run coverage html
