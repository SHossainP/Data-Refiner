import sqlite3
import pandas as pd
from datetime import datetime
from Data_Preprocessor.logger import get_logger

logger = get_logger()
DB_NAME = 'csv_data.db'

def initialize_database():
    """
    Creates the SQLite database and table if it does not exist.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Date TEXT,
            Product TEXT,
            Sales REAL,
            Revenue REAL,
            saved_at TEXT
        )
    """)

    conn.commit()
    conn.close()
    logger.info("✅ Database initialized successfully.")


def save_to_database(data: pd.DataFrame) -> None:
    """
    Saves cleaned sales data into the database.

    Args:
        data (pd.DataFrame): The cleaned DataFrame to be saved.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    saved_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        
        # Save to database
        data.to_sql("sales_data", conn, if_exists="append", index=False)  

        logger.info(" Data saved to database successfully.")

    except Exception as e:
        logger.error(f" Error saving data to database: {e}")

    finally:
        conn.close()
