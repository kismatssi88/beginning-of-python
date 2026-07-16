import pandas as pd
df = pd.read_csv("pandas/footballers.csv")
print("The descriptive statistics of the data is:")
print(df.describe())