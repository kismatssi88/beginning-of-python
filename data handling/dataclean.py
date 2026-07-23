import pandas as pd
import numpy as np

#reading
df=pd.read_csv("data handling/csvdata.csv")
print("reading values")
print(df.head())

#finding missing values
print("showing missing values")
print(df.isnull().sum()) # give coount of missing values

#filling parental education 

df["parental_education"] = df["parental_education"].fillna(
    df["parental_education"].mode()[0]
)
#finding missing values
print("showing missing values")
print(df.isnull().sum()) # give coount of missing values
