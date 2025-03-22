# Data-Refiner
📌 CSV Data Preprocessing with Automation
Project Overview
This project automates the preprocessing of CSV files by filtering, cleaning, and storing the data efficiently. It processes multiple CSV files in a directory and saves the cleaned outputs with dynamically generated filenames based on the year present in the input filenames. The cleaned data is stored both as CSV files and in an SQLite database for structured querying.

🎯 Features
✅ Batch Processing: Processes all CSV files in a directory automatically.
✅ Data Filtering: Removes rows with missing 'Date' or 'Product' values.
✅ Missing Value Imputation: Fills missing 'Sales' and 'Revenue' using column median.
✅ Database Storage: Saves processed data into an SQLite database for structured retrieval.
✅ Dynamic Output Naming: Generates filenames as cleaned_<year>.csv.
✅ Automatic Directory Handling: Creates an output directory if it doesn’t exist.
✅ Logging System: Tracks each processing step and errors for debugging.

📄 Logging System
All logs are stored in data_preprocessing.log, tracking:
🔹 INFO: Normal operations like filtering and saving.
🔹 WARNING: Non-critical issues such as missing values handled with imputation.
🔹 ERROR: Failures like missing input files or database errors.

📂 Project Structure
graphql
Copy code
📁 Dat_Preprocessor
│── filter.py         # Filters data based on required columns
│── imputation.py     # Handles missing value imputation
│── database.py       # Manages SQLite database operations
│── logger.py         # Implements logging system
│── main.py           # CLI entry point for execution
│── requirements.txt  # Dependencies
│── README.md         # Project documentation
🚀 Installation & Usage
1️⃣ Setup Environment
sh
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
2️⃣ Run the Script
sh
Copy code
python main.py files/ output_files/
3️⃣ Query Cleaned Data (Example SQLite Query)
sql
Copy code
SELECT * FROM sales_data WHERE Product = 'Laptop';
🤖 Why CSV Preprocessing is Important?
🔹 Data Cleaning & Transformation: Ensures structured and error-free data.
🔹 Automated Processing: Saves time by handling large datasets efficiently.
🔹 Better Analysis & Machine Learning: Provides clean data for insightful analysis.
🔹 Database Storage: Enables structured querying and retrieval of processed data.

This project provides an automated, scalable, and efficient solution for CSV data preprocessing, making data ready for analysis and machine learning tasks
