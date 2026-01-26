#enumerator used to get both indiex and value in this function we can set starting index value
l2=["india","uk","usa","germany","france"]
for i,j in enumerate(l2):
    print(i,j)

l1=["a",'b','c','d','e']
for i,j in enumerate(l1):
    print(i,j)

l=[1,2,3,4,5]
for i,j in enumerate(l,10):
    print(i,j)
#in enumrfator we can set the starting value from which number we want to start


l3=["hi","hello"]
for i,j in enumerate(l3,0):
    print(i,j)

l=[1,2,3,4,45,5,6]
for i,j in enumerate(l,900):
    print(i,j)