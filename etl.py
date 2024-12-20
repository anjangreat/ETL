
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy import create_engine

def extract_from_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"Data successfully extracted from {file_path}.")
        return data
    except Exception as e:
        print(f"Error extracting data from CSV: {e}")

def transform_data(data):
    try:
        data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')

        data.fillna(data.mean(), inplace=True)
        print("Data successfully transformed.")
        return data
    except Exception as e:
        print(f"Error during transformation: {e}")

def load_to_database(data, table_name, connection_string):
    try:
        engine = create_engine(connection_string)
        data.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Data successfully loaded into the table {table_name}.")
    except Exception as e:
        print(f"Error loading data into database: {e}")

def etl_process(file_path, table_name, connection_string):
    print("Starting ETL process...")
    
    data = extract_from_csv(file_path)
    
    if data is not None:
        data = transform_data(data)
    if data is not None:
        load_to_database(data, table_name, connection_string)
    
    print("ETL process completed.")

if __name__ == "__main__":
    file_path = "Fuel_cell_performance_data-Full.csv"  
    table_name = "fuel_cell_data"  
    connection_string = "sqlite:///fuel_cell_database.db"  

    etl_process(file_path, table_name, connection_string)
