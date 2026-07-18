import pandas as pd
stud={
    "age":[20,22,None,26,None],
    "marks":[20,30,None,50,60],
}
df =pd.DataFrame(stud)

#linear method
df.interpolate(method="linear",axis=0,inplace=True)
print(df)

df["age"]=df['age'].interpolate(method='linear')
print(df)