# CI/CD PySpark Pipeline

This project implements a CI/CD pipeline using GitHub Actions to process customer data with PySpark. The pipeline includes steps for data preprocessing, splitting, and artifact storage.

## Project Structure

```
ci-cd-pyspark-pipeline
├── .github
│   └── workflows
│       └── ci.yml          # GitHub Actions workflow configuration
├── src
│   ├── __init__.py         # Marks the directory as a Python package
│   ├── pipeline.py         # Main entry point for the data processing pipeline
│   ├── preprocess.py       # Functions for data loading and cleaning
│   └── split.py            # Functions for splitting data into training and testing sets
├── tests
│   └── test_preprocess.py   # Unit tests for preprocessing functions
├── data
│   ├── raw
│   │   └── customers-1000.csv # Source dataset
│   └── processed            # Directory for processed datasets
├── scripts
│   └── run_local.sh        # Shell script to run the pipeline locally
├── requirements.txt        # Project dependencies
├── .gitignore              # Files and directories to ignore in Git
└── README.md               # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ci-cd-pyspark-pipeline
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the pipeline locally:
   ```
   bash scripts/run_local.sh
   ```

## Usage

The pipeline processes the `customers-1000.csv` file by:
- Removing repeated rows and empty values.
- Renaming the first column to "target".
- Splitting the data into training and testing datasets.

The processed datasets will be saved in the `data/processed` directory.

## CI/CD Integration

The GitHub Actions workflow defined in `.github/workflows/ci.yml` automates the execution of the pipeline on code changes, ensuring that the data processing steps are consistently applied and the resulting datasets are uploaded to the GitHub Actions artifact storage.