import pandas as pd
df = pd.read_csv("data handling/csvdata.csv")
 


# Convert to Excel
df.to_excel("data handling/csvdata.xlsx", index=False)

print("CSV converted to Excel successfully!")