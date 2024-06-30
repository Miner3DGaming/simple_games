#!/bin/bash

# Get file location of itself
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"

PYTHON_INTERPRETER="$SCRIPT_DIR/data/interpreter/python_interpreter_console.exe"

PYTHON_SCRIPT="$SCRIPT_DIR/data/hello_world.py"

# Execute the Python script using the specified interpreter, this is a pain
"$PYTHON_INTERPRETER" -file "$PYTHON_SCRIPT"