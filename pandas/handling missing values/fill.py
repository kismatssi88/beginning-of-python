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

#filing with default values
df.fillna(1,inplace=True)
print(df)

#filling my own values putting mean of  age 
df['Age'].fillna(df['Age'].mean(),inplace=True)
print(df)

#filling median in fifa ratings 
df['fifa rating'].fillna(df["fifa rating"].median(),inplace=True)
print(df)