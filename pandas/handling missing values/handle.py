import pandas as pd
footballers={
    "Name": ["Lionel Messi","yamal","Cristiano Ronaldo",None,"Kylian Mbappe"],
    "Age": [39, 19, 41, None, 28],
    "Nationality": ["Argentinian", "Spanish", "Portuguese", "Brazilian", "French"],
    "position": ["Right Winger", "right Winger", "striker", "Left Winger", "striker"],
    "preferred_foot": ["Left", "left", "Right", "Left", "Right"],
    "fifa rating": [91, 87, None, 88, 92],
}
df = pd.DataFrame(footballers)
#removing rows with missing values
df.dropna(axis=0,inplace=True)
print(df)

#removing columns with missing values
df.dropna(axis=1,inplace=True)
print(df)