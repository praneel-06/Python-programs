import numpy as np
#slicing and most list functions can be used on numpy list and is mutable
a=np.array([1,2,3,4,5,6,7,8,9])
b=a[2:]
b[0]=40
print (a)
#we have created a new array b and stored the value of a in b, 
#but what is observed is when we change elements in b, elements in a are also modified
c=[1,2,3,4,5,6,7,8,9]
d=c[3:]
d[0]=40
print (c)
#does not change for a normal list modification

