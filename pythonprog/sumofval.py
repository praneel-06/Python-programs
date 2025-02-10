d={}
n=int(input("enter number of keys in dictionairy"))
for i in range (n):
    key=input("enter key")
    val=int(input("enter integer value"))
    d.update({key:val})
sum=0
for values in d.values():
    sum=sum+values
print("sum of values in dictionairy is:",sum)