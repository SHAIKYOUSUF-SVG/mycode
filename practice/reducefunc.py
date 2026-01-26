import functools
from functools import reduce

list1=[1,2,3,4,5,6]
#out=functools.reduce(lambda i,j:i+j,list1)
out=reduce(lambda i,j:i+j,list1)
print(out)

a=map(lambda i:i+1 ,list1 )
b=filter(lambda i:i%2==0,list1)
print(list(a))
print(list(b))