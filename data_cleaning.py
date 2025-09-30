
import pandas as pd
from tabulate import tabulate   

# 1. Load dataset
df = pd.read_csv("marketing_campaign.csv")  
print("First 5 rows of the dataset:")
print(tabulate(df.head(), headers='keys', tablefmt='pretty'))

# 2. Check dataset information
print("\nDataset Info:")
print(df.info())

# 3. Check for missing values
print("\nMissing values in each column:")
missing = df.isnull().sum().reset_index()
missing.columns = ["Column", "Missing_Count"]
print(tabulate(missing, headers="keys", tablefmt="pretty"))

# 4. Handle missing values
if 'Income' in df.columns:
    df['Income'] = df['Income'].fillna(df['Income'].median())

df = df.dropna()

# 5. Remove duplicate rows
df = df.drop_duplicates()

# 6. Standardize text values
if 'Marital_Status' in df.columns:
    df['Marital_Status'] = df['Marital_Status'].str.strip().str.title()

if 'Education' in df.columns:
    df['Education'] = df['Education'].str.strip().str.title()

# 7. Fix date formats
if 'Dt_Customer' in df.columns:
    df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], dayfirst=True)

# 8. Rename columns
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 9. Fix data types
if 'year_birth' in df.columns:
    df['year_birth'] = df['year_birth'].astype(int)

# 10. Save cleaned dataset
df.to_csv("marketing_campaign_cleaned.csv", index=False)

# 11. Show final cleaned data sample
print("\nCleaned dataset sample (first 10 rows):")
print(tabulate(df.head(10), headers='keys', tablefmt='pretty'))

print("\n Data cleaning complete. Cleaned dataset saved as 'marketing_campaign_cleaned.csv'")

