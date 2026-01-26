l2=["india","uk","us","germany","france"]
out={i:len(i) for i in l2}
print(out)


out1={i:l2[i] for i in range(len(l2))}
print(out1)


l1=["a",'b','c','d','e']
l2=["india","uk","us","germany","france"]
out2={i:j for i in l1 for j in l2}  #zip function is better for this
print(out2)


l=["hi","hello",89]
out={str(i):len(str(i)) for i in l}
print(out)


l3=[2,3,4,5,6,7]
#for i in range(100):
out={i:i*i for i in range(1,101) if i%2==0 and i*i%2==0}
print(out)


out1={i:i*i for i in range(1,100) if i*i<=100}
print(out1)


out2={i for i in l3 if i%2==0}
print(out2)