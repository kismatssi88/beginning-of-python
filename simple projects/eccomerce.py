import pandas as pd
df=pd.read_csv('simple projects\Ecommerce Purchases')

 #showing top 10 rows of dataset
print(df.head(10))
#showing bottom 10 rows
print(df.tail(10))

#data type of each columns
print(df.info())

#no. of rows and columns i.e. shape
print(df.shape)

#checking null values
print(df.isnull().sum())

#highest and lowest purchase price which means filtering
print(df['Purchase Price'].min())
print(df['Purchase Price'].max())

#average purchase price
print(df['Purchase Price'].mean())

#people having fr as there  language which is french
filter=(df['Language']=='fr').sum()
print("The number of people who speak french are",filter)

#people those who are engineers
filter=(df['Job']=="Engineer").sum()
print("The total numbers of enginners are:",filter)

# Email of a person with ip adress 132.207.160.22
email=df.loc[df["IP Address"] == "132.207.160.22", "Email"]
print('Email of a person with ip adress 132.207.160.22',email)

#number People have Mastercard as their Credit Card Provider and made a purchase above 50
total=df[(df['CC Provider']=="Mastercard")& (df['Purchase Price']>50)]
print("The total numbers of people are:",total)

# Email of a person with Credit Card Number: 4664825258997302
print(df.loc[df["Credit Card"] == 4664825258997302, "Email"])
print("Email of a person with Credit Card Number: 4664825258997302",email)

 # people purchase during the AM and how many people purchase during PM
print(df["AM or PM"].value_counts())