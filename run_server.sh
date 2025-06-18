#!/bin/bash
# Script to run the Zentickr MCP server in the virtual environment

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Activate the virtual environment
source env/bin/activate

# Run the server
python run_server.py

# Deactivate the virtual environment when done
deactivate