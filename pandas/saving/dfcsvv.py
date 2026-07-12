import pandas as pd
data = {
    "Name": ["kessi", "messi", "kane", "ronaldo"],
    "Age": [25, 30, 35, 40],            
    "city": ["jhapa", "ktm", "btm", "brt"],
    "height": [5.5, 6.0, 5.9, 6.1]
}
df = pd.DataFrame(data)
print(df)
df.to_csv("pandas/employees.csv", index=False)
df.to_json("pandas/employees.json", index=False)
df.to_excel("pandas/employees.xlsx", index=False)