d={}
n=int(input("enter number of keys in dictionairy"))
for i in range(n):
    key=input("enter key: ")
    val=int(input("enter value: "))
    d.update({key:val})
print (d)