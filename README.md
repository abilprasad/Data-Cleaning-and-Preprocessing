# Data-Cleaning-and-Preprocessing
Task 1: Data Cleaning and Preprocessing
# Mall Customers Data Cleaning Script




The cleaning script performs the following steps:

1. Load the dataset from Excel.
2. Identify and handle missing values:
   - Numeric columns → filled with mean.
   - Categorical columns → filled with mode.
3. Remove duplicate rows.
4. Standardize text values (e.g., gender formatting).
5. Convert date columns to a consistent **dd-mm-yyyy** format.
6. Rename column headers to lowercase with underscores.
7. Fix data types:
   - Age → integer
   - Annual income → float
   - Spending score → integer
8. Final quality checks for data types and missing values.
9. Save the cleaned dataset as a new Excel file.

---

## Files in This Repository

- `Mall_Customers.xlsx` — Raw dataset (input)
- `mall_customers_cleaning.py` — Python script for cleaning the dataset
- `Mall_Customers_Cleaned.xlsx` — Output cleaned dataset (optional to include)
- `README.md` — Documentation for the project

---

## Requirements

Make sure you have Python installed along with the following libraries:



