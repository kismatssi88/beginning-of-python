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
print(df)
print(df.isnull())
print(df.isnull().sum())
print(df.isnull().Name)