import pandas as pd
data1 = pd.DataFrame({
    "id":[11,12],
    "name":["kessi","messi"],
})

data2=pd.DataFrame({
    "id":[22,23],
    "name":["ayush","siddu"],

})

#rows wise
df_concat =pd.concat([data1,data2],axis=0 ,ignore_index=True)
print(df_concat)


#column wise
df_concat =pd.concat([data1,data2],axis=1 ,ignore_index=False)
print(df_concat)