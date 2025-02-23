import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\doktu\expense-tracker\transactions.csv"
df = pd.read_csv(file_path)

# Check actual column names
print("Original column names:", df.columns)

# Strip spaces from column names
df.columns = df.columns.str.strip()

# Rename columns
df.rename(columns={
    "Operation #": "Operation Number",
    "Value date": "Date",
    "Sender/Beneficiary": "Type of Transaction",
    "Description": "Description",
    "Balance": "Adjusted Amount",
}, inplace=True)

# Ensure 'Date' column exists before converting
df["Date"] = pd.to_datetime(df["Date"], format="%d.%m.%Y", errors="coerce").dt.strftime("%d.%m.%Y")

# Identify deposits and expenses
df["Amount"] = pd.to_numeric(df["Amount"], errors='coerce')  # Convert Amount to numeric
df["Transaction Type"] = df["Amount"].apply(lambda x: "Deposit" if x > 0 else "Expense")

# Check columns
print(df.columns)

# Check variables in new column Transaction Type
print(df["Transaction Type"].unique())

df.to_excel("cleaned_transactions.xlsx", index=False)

# 🔹 Data Adjustments Due to Banking Inconsistencies
# --------------------------------------------------
# Some variable values related to deposits and expenses were manually adjusted
# due to irregularities in bank transaction records.
#
# The "Adjusted Amount" column represents the sum or difference of the
# transaction amounts above it. However, in certain cases, incorrect or
# zero values appeared.
#
# Example Issue:
# - Some transfers to another account were recorded as positive amounts,
#   leading to them being incorrectly classified as "Deposits."
#
# While such inconsistencies could be handled programmatically in Python,
# trust me—sometimes manual adjustments are the best approach when working
# with Kyrgyz banks. With 10 years of experience in this, I can confirm! 😆





