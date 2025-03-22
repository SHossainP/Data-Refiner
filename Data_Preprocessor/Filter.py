
import pandas as pd
import os
from Data_Preprocessor.logger import get_logger

logger = get_logger()

def filter_data(input_path: str) -> pd.DataFrame:
    """
    Reads a CSV file, filters required columns, removes missing values, 
    and processes the 'Date' and 'Product' columns.

    Steps:
    1. Checks if the file exists.
    2. Reads the CSV file into a DataFrame.
    3. Keeps only the required columns: 'Date', 'Product', 'Sales', 'Revenue'.
    4. Drops rows with missing 'Date' or 'Product'.
    5. Removes semicolons from 'Product' names.
    6. Converts 'Date' column to a standardized format (YYYY-MM-DD).

    Args:
        input_path (str): The file path of the input CSV.

    Returns:
        pd.DataFrame: The filtered DataFrame with cleaned data.
                      Returns an empty DataFrame if an error occurs.
    """
    required_columns = ['Date', 'Product', 'Sales', 'Revenue']
    
    try:
        if not os.path.exists(input_path):
            logger.error(" Error: File not found at %s", input_path)
            return pd.DataFrame()
        # Read CSV file
        data = pd.read_csv(input_path)

        # Keep only required columns
        data = data[required_columns]

        # Remove rows where 'Date' or 'Product' is empty
        data.dropna(subset=['Date', 'Product'], inplace=True)
       
        
        data['Product'] = data['Product'].astype(str).str.replace(";", "", regex=True)

        # Convert 'Date' column to standard format
        data['Date'] = pd.to_datetime(data['Date'], errors='coerce').dt.strftime('%Y-%m-%d')

        return data  #  Correctly returning filtered DataFrame

    except FileNotFoundError:
        logger.error(f"Error: File not found at {input_path}")
        return pd.DataFrame()  #  Return empty DataFrame on error

    except Exception as e:
        logger.error(f"Error processing CSV: {e}")
        return pd.DataFrame()  #  Return empty DataFrame on error
