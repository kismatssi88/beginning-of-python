import pandas as pd
footballers={
    "Name": ["Lionel Messi","yamal","Cristiano Ronaldo","Neymar Jr","Kylian Mbappe"],
    "Age": [39, 19, 41, 32, 28],
    "Nationality": ["Argentinian", "Spanish", "Portuguese", "Brazilian", "French"],
    "position": ["Right Winger", "right Winger", "striker", "Left Winger", "striker"],
    "preferred_foot": ["Left", "left", "Right", "Left", "Right"],
    "fifa rating": [91, 87, 90, 88, 92],
}

df=pd.DataFrame(footballers)

#sorting  single coulmns
df.sort_values(by='Age',ascending=True,inplace=True)
print(df)

#sorting multiple columns

df.sort_values(by=['Age','fifa rating'],ascending=False,inplace=False)
print(df)

#one ascending another descending 
df.sort_values(by=['Age','fifa rating'],ascending=[True,False],inplace=False)
print(df)
