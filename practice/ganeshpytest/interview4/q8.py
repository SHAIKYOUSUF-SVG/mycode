
#filter is returns if it is true
# here true values wil get as output
#in filter we get only if object is true
data=["india",5,0,0.8,0.0,False]
out=filter(lambda i:i,data)
print(list(out))