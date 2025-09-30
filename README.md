# marketing_campaign-cleaning
# Customer Personality Analysis – Data Cleaning

This project is part of a Data Analyst Internship Task.
The goal is to clean and preprocess the raw "Customer Personality Analysis" dataset to make it ready for analysis and modeling.

The raw dataset had issues like missing values, duplicates, inconsistent formatting, and unclean column names.
Using Python (Pandas), these issues were fixed and the cleaned dataset was saved for further analysis.

##  Steps Performed

1. Loaded Dataset

   * File: "marketing_campaign.csv".
   * Used Pandas to read the dataset.

2. Checked Missing Values

   * Found null values in the 'Income' column.
   * Replaced missing incomes with the median value.

3. Removed Duplicates

   * Duplicate rows were dropped using Pandas.

4. Standardized Text Columns

   * Cleaned up 'Marital_Status' and 'Education' values
   * Example: converted 'single' → "Single", 'Phd' → "Phd"

5. Fixed Date Format

   * Converted 'Dt_Customer' column to proper 'datetime' format.

6. Renamed Columns

   * All column names converted to lowercase with underscores.
   * Example: 'Year_Birth' → 'year_birth'.

7. Checked and Fixed Data Types

   * Ensured 'year_birth' is stored as an integer.

8. Saved Cleaned Dataset

   * Output file: "marketing_campaign.csv".

##  Files in this Repository

* "marketing_campaign.csv"→ Raw dataset (original file).
* 'task1_cleaning.py' → Python script for cleaning.
* "marketing_campaign_cleaned.csv". → Final cleaned dataset.
* 'README.md' → Documentation (this file).

##  How to Run

1. Install requirements (only Pandas and Tabulate are used):
   pip install pandas tabulate
   
2. Run the script:
   python task1_cleaning.py
   
3. The cleaned dataset will be saved as "marketing_campaign_cleaned.csv" .


##  Deliverables

* A clean, structured dataset ready for analysis.
* A reproducible Python script for data cleaning.
* Documentation of steps taken (this README).

##  Key Learnings

* Handling missing values (dropna, fillna).
* Removing duplicates.
* Standardizing categorical values.
* Fixing date formats and data types.
* Saving and documenting cleaned datasets.
