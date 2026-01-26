#using 2 for loops
#its better to use 1 loop dont useit 2loops

data1=[10,20]
data2=["india","uk"]

out=[(i,j) for i in data1 for j in data2]
print(out)