import pandas as pd
data ={
     'name':['kismat','messi','yamali','siddu','kussuu'],
     'age':[20,30 ,22,21,23],
     'gender':['male','male','female','male','female'],
     'weight':[50,60 , 88,65,77],
}
df=pd.DataFrame(data)
print(df)

#displaying top rows
print(df.head(3))

#displaying bottom rows
print(df.tail(3))

# info() it finds rows ,columns .data types
print(df.info())

#describe() give statistics description of data
print(df.describe())

#shape()find size of data (rows ,columns) ixj
print(df.shape)

#cheking whether nulll vlaues or not
print(df.isnull())
print(df.isnull().sum())

#finding unique values 
print(df['gender'].unique())
print(df['gender'].nunique())

#age betwenn 20 to 25
filter=df[df['age']<=25]
print(filter)