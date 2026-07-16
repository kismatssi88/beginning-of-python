import pandas as pd
df = pd.read_csv("pandas/annual.csv")
print(df.head())
print(df.shape)
print(df.describe())
print(df.columns)