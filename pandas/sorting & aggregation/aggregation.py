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

total_sum=df['Age'].sum()
print('the total sum is')
print(total_sum)

mean_fifarating=df['fifa rating'].mean()
print('the mean is ')
print(mean_fifarating)