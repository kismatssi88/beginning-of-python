import pandas as pd

footballers = {
    "Name": ["Lionel Messi", "Yamal", "Cristiano Ronaldo", "Neymar Jr", "Kylian Mbappe"],
    "Age": [39, 19, 41, 32, 28],
    "Nationality": ["Argentinian", "Spanish", "Portuguese", "Brazilian", "French"],
    "Position": ["Right Winger", "Right Winger", "Striker", "Left Winger", "Striker"],
    "Preferred_Foot": ["Left", "Left", "Right", "Left", "Right"],
    "FIFA_Rating": [91, 87, 90, 88, 92],
}

df = pd.DataFrame(footballers)

print("Original DataFrame:")
print(df)

# Group by Position
group = df.groupby("Position")

# Mean of Age and FIFA Rating
print("\nMean:")
print(group[["Age", "FIFA_Rating"]].mean())

# Sum of Age and FIFA Rating
print("\nSum:")
print(group[["Age", "FIFA_Rating"]].sum())