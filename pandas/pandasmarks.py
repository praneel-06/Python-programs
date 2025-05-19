import pandas as pd

data = {
    "Roll Number": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": ["Aarav", "Bhavya", "Charan", "Diya", "Eshaan", "Fatima", "Gopal", "Hina", "Ishaan", "Jiya"],
    "Gender": ["M", "F", "M", "F", "M", "F", "M", "F", "M", "F"],
    "Marks1": [85, 90, 78, 88, 92, 75, 80, 95, 89, 87],
    "Marks2": [78, 82, 33, 79, 90, 23, 76, 91, 83, 86],
    "Marks3": [88, 85, 90, 92, 80, 87, 89, 84, 77, 91]
}
df=pd.DataFrame(data)
print(df.index)(0,4,1)
print(df)
nameH=df.loc[0,"Name"]
nameL=df.loc[0,"Name"]
nameA=df.loc[0,"Name"]
high=df.loc[0,"Marks2"]
low=df.loc[0,"Marks1"]
sum=avg=0
df["Total Marks"]=df["Marks1"]+df["Marks2"]+df["Marks3"]
df["Average"]=df["Total Marks"]/3
fail=[]
highavg=df.loc[0,"Average"]
for i in df.index:
    if(df.loc[i,"Marks2"]>high):
        high=df.loc[i,"Marks2"]
        nameH=df.loc[i,"Name"]
    if(df.loc[i,"Marks1"]<low):
        low=df.loc[i,"Marks1"]
        nameL=df.loc[i,"Name"]
    sum=sum+df.loc[i,"Marks3"]
    if(df.loc[i,"Average"]>highavg):
        highavg=df.loc[i,"Average"]
        nameA=df.loc[i,"Name"]
    if(df.loc[i,"Marks2"]<40):
        fail.append(df.loc[i,"Name"])
avg=sum/10
print("Student with lowest (Marks1)",nameL,low)
print("Student with highet (Marks2)",nameH,high)
print("Student avg marks (Marks3)",avg)
print("Student who failed (Marks2)",fail)


