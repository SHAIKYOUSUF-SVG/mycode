list1=[1,2,3,4,5,6]
out=filter(lambda i:i%2==0,list1)
print(list(out))


out1=filter(lambda i:i%2!=0,list1)
print(list(out1))


#filter function used to filter values from iterable

l2=[12,23,42,12,44,32,88]
out=filter(lambda i:i%2==0,l2)
print(list(out))

l1=[1,2,3,4,5,56,7]
out=filter(lambda i:i%2==0,l1)
print(list(out))


l3=[23,4,5,33,23,455]
out=filter(lambda i:i%2!=0,l3)
print(list(out))