# Import pandas and matplotlib.pyplot.
import pandas as pd
import matplotlib.pyplot as plt
# Setting file file directory to our source data

file_path = r"C:\Users\tima.dokturbekuulu\expense-tracker\transactions.csv"
df = pd.read_csv(file_path)
print(df.head())
