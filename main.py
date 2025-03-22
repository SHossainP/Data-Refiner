import argparse
import pandas as pd
import os
import re
from Data_Preprocessor.Filter import filter_data
from Data_Preprocessor.Imputation import fill_missing_values
from Data_Preprocessor.database import initialize_database
from Data_Preprocessor.logger import get_logger

# Initialize logger
logger = get_logger()

def extract_year_from_filename(filename: str) -> str:
    """
    Extracts the first four-digit year found in the filename.
    """
    match = re.search(r'\d{4}', filename)
    return match.group(0) if match else "unknown"

def process_files(input_dir: str, output_dir: str):
    """
    Processes all CSV files in the input directory and saves cleaned files in the output directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        logger.info(f"Created output directory: {output_dir}")
    
    # Initialize Database
    logger.info("Initializing database...")
    initialize_database()
    
    # Get all CSV files from the input directory
    csv_files = [f for f in os.listdir(input_dir) if f.endswith(".csv")]
    
    if not csv_files:
        logger.error("No CSV files found in the input directory.")
        return
    
    for file in csv_files:
        input_file = os.path.join(input_dir, file)
        year = extract_year_from_filename(file)
        output_file = os.path.join(output_dir, f"cleaned_{year}.csv")
        
        logger.info(f"Processing file: {input_file}")
        
        # Step 1: Apply Filtering
        filtered_data = filter_data(input_file)
        if filtered_data.empty:
            logger.error(f"Skipping {file}: No valid data after filtering.")
            continue
        
        # Step 2: Apply Imputation
        cleaned_data = fill_missing_values(filtered_data)
        if cleaned_data is None or cleaned_data.empty:
            logger.error(f"Skipping {file}: No valid data after imputation.")
            continue
        
        # Step 3: Save the final cleaned data
        cleaned_data.to_csv(output_file, index=False)
        logger.info(f" Processed file saved: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch Data Preprocessing Pipeline")
    parser.add_argument("input_dir", help="Path to the directory containing input CSV files")
    parser.add_argument("output_dir", help="Path to the directory to save cleaned CSV files")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_dir):
        logger.error(" Error: Input directory does not exist!")
    else:
        logger.info(f"Starting Data Preprocessing for files in: {args.input_dir}")
        process_files(args.input_dir, args.output_dir)
        logger.info("All files processed successfully!")
