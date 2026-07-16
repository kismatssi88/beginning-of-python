import pandas as pd


footballers={
    "Name": ["Lionel Messi","yamal","Cristiano Ronaldo","Neymar Jr","Kylian Mbappe"],
    "Age": [39, 19, 41, 32, 28],
    "Nationality": ["Argentinian", "Spanish", "Portuguese", "Brazilian", "French"],
    "position": ["Right Winger", "right Winger", "striker", "Left Winger", "striker"],
    "preferred_foot": ["Left", "left", "Right", "Left", "Right"],
    "fifa rating": [91, 87, 90, 88, 92],
}
df = pd.DataFrame(footballers)
print(df)

# to csv
df.to_csv("pandas/footballers.csv", index=False)
 
# to json 
df.to_json("pandas/footballers.json")

# to excel
df.to_excel("pandas/footballers.xlsx", index=False)