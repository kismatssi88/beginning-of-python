import pandas as pd
stud={
    "marks":[90, 80, 70, 60],   
    "name":["kessi", "messi", "kane", "ronaldo"],
    "id":[1, 2, 3, 4],
    "city":["jhapa", "ktm", "btm", "brt"]

}
df=pd.DataFrame(stud)
print(df)
df.to_excel("student.xlsx", index=False)
            


