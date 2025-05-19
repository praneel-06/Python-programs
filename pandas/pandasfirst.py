import pandas as pd
diction={1:["S1","S2","S3","S4"],"Num":[20,22,23,24],"Sub":["math","sci","eng","soc"]}
df = pd.DataFrame(diction)
print(df)

print(df.head(1))
print(df.coloumns())

