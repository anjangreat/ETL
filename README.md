This project implements a simple ETL (Extract, Transform, Load) pipeline in Python. It demonstrates how to extract data from a CSV file, perform basic transformations, and load the processed data into a database.

Workflow

1. Extraction

Reads data from a CSV file.

Uses pandas to load the data into a DataFrame.

2. Transformation

Standardizes column names to lowercase and replaces spaces with underscores.

Handles missing values by replacing them with the mean of their respective columns.

3. Loading

Loads the transformed data into a specified database table.

Uses SQLAlchemy for database connectivity and loading.

Requirements

Software

Python 3.7+

Libraries

pandas

numpy

sqlalchemy

Install the required libraries using:

pip install pandas numpy sqlalchemy

Instructions

Set up the source CSV file:

Ensure the source data file (e.g., Fuel_cell_performance_data-Full.csv) is in the same directory as the script or update the file path in the script.

Set up the database:

By default, the script uses an SQLite database (fuel_cell_database.db). Update the connection string for other database systems.

Run the ETL script:

Execute the Python script using:

python etl_pipeline.py

Verify the data in the database:

Open the database and inspect the table (e.g., fuel_cell_data) to ensure the data is loaded correctly.

Example Usage

Input

Source CSV file: Fuel_cell_performance_data-Full.csv

Parameters

Table Name: fuel_cell_data

Database Connection: sqlite:///fuel_cell_database.db

Output

Transformed data loaded into the fuel_cell_data table in the SQLite database.
