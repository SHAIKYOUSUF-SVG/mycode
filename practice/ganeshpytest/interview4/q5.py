#take alist and len(list) is even return1 else return 0

func=lambda inp: 1 if (len(inp) %2==0 and type(inp) ==list) else 0
data=[10,20,40,30]
out=func(data)
print(out)
print("#################")


out=lambda inp: 1 if (type(inp)==list) else 0
data1=["yousuf"]
print(out(data))

#we dont use this for multiline function