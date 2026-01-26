data1=[10,20,30,40,50,60]
data2=["a","b","c"]


out=map(lambda i,j:[i,j], data1,data2)
print(list(out))
#output
#[[10, 'a'], [20, 'b'], [30, 'c']]
