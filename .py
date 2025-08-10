

import pandas as pd

df = pd.read_excel("/content/Mall_Customers.xlsx")  


print("\n--- Missing values before cleaning ---")
print(df.isnull().sum())

for col in df.columns:
    if df[col].dtype == "object":
        df[col].fillna(df[col].mode()[0], inplace=True)  
    else:
        df[col].fillna(df[col].mean(), inplace=True)     

df.drop_duplicates(inplace=True)

if "Gender" in df.columns:
    df["Gender"] = df["Gender"].str.strip().str.capitalize()

for col in df.columns:
    if "date" in col.lower():
        df[col] = pd.to_datetime(df[col], errors="coerce")
        df[col] = df[col].dt.strftime("%d-%m-%Y") 

df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]


if "age" in df.columns:
    df["age"] = df["age"].astype(int)

if "annual_income_(k$)" in df.columns:
    df["annual_income_(k$)"] = df["annual_income_(k$)"].astype(float)

if "spending_score_(1-100)" in df.columns:
    df["spending_score_(1-100)"] = df["spending_score_(1-100)"].astype(int)

print("\n--- Data types after cleaning ---")
print(df.dtypes)

print("\n--- Missing values after cleaning ---")
print(df.isnull().sum())

output_file = "Mall_Customers_Cleaned.xlsx"
df.to_excel(output_file, index=False)
print(f"\nCleaned file saved as '{output_file}'")
