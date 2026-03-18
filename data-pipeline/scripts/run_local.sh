#!/bin/bash

# Activate the virtual environment if needed
# source venv/bin/activate

# Run the PySpark pipeline
python src/pipeline.py

# Notify the user that the process is complete
echo "Data processing pipeline executed successfully."
