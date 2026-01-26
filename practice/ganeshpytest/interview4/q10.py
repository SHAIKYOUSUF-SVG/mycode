data1=[10,20,30]
data2=["a","b","c"]
'''
out=zip(data1,data2)
print(list(out))


for i,j in enumerate(data1):
    print(i,j)'''

out=map(lambda i,j: [i,j],data1,data2)
out=map(lambda i,j: {i,j},data1,data2)
print(list(out))