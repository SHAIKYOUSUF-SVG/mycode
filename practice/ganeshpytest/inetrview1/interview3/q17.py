daata=["india","uk","germany"]

#two different methdos
out={i:len(i) for i in daata}

print(out)


out=[[i,len(i)] for i in daata]
print(dict(out))