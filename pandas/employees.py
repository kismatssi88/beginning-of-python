import pandas as pd
employees={
    "Name":["messi","kessi","jude","yamal","pedri"],
    "age":[32,28,21,17,21],
    "salary":[50000,70000,100000,800000,200000],
}
df = pd.DataFrame(employees)
print(df)

print("the age column is:")
col=df["age"]
print(col)

#filering rows salary less than 60,000 single condition 
filter_row=df[df["salary"]<60000]
print(filter_row)

#multiple conditoon
fill_row = df[(df["salary"]>60000)& (df["salary"]<10000)]
print(fill_row)