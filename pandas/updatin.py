import pandas as pd
footballers={
    "Name": ["Lionel Messi","yamal","Cristiano Ronaldo","Neymar Jr","Kylian Mbappe"],
    "Age": [39, 19, 41, 32, 28],
    "Nationality": ["Argentinian", "Spanish", "Portuguese", "Brazilian", "French"],
    "position": ["Right Winger", "right Winger", "striker", "Left Winger", "striker"],
    "preferred_foot": ["Left", "left", "Right", "Left", "Right"],
    "fifa rating": [91, 87, 90, 88, 92],
}

#single value update
df = pd.DataFrame(footballers)
df.loc[0,"fifa rating"]=99 
print(df)

#updating the entire columns we get
df['Age']=df['Age']+4
print(df)