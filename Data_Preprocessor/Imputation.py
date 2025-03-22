

import pandas as pd
from Data_Preprocessor.logger import get_logger
from Data_Preprocessor.database import save_to_database

logger = get_logger()
def fill_missing_values(data: pd.DataFrame) -> pd.DataFrame:
    """
    Imputes missing values in the 'Sales' and 'Revenue' columns using their median values.

    Steps:
    1. Checks if 'Sales' and 'Revenue' columns have missing values.
    2. Replaces missing values with the column median.
    3. Saves the cleaned data to the database.
    4. Returns the cleaned DataFrame.

    Args:
        data (pd.DataFrame): The input DataFrame containing sales data.

    Returns:
        pd.DataFrame: The cleaned DataFrame with imputed values.
                      Returns None if an error occurs.
    """
    try:
        # Fill missing 'Sales' and 'Revenue' with column median
        for column in ['Sales', 'Revenue']:
            if data[column].isnull().sum() > 0:  # Check if there are missing values
                median_value = data[column].median()
                data[column].fillna(median_value, inplace=True)

        # Return cleaned data instead of saving
        cleaned_data = data.copy()
        save_to_database(cleaned_data)
        logger.info("Missing values imputed and data saved to database successfully.")

        return cleaned_data
        

        
    except Exception as e:
        logger.error(f"Error processing data: {e}")
        return None  # Return None if an error occurs
