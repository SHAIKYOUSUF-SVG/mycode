l1=["a",'b','c','d','e']
l2=["india","uk","us","germany","france","itely"]
d={}

for i,j in zip(l1,l2):
    print(i,j)
    d[j]=i
print(d)