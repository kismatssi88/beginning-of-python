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
df["New rating"]=df["fifa rating"]+2
print(df)

#using insert it helps to put the columns in specific positions so 
df.insert(0,"goat ranking",[1,2,3,4,5])
print(df)