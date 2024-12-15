#what is lamda function? related to functions
#means:function in a singel line is lamda function
# also called a sanonomious function
'''
def func(x):
    return x+1
'''
#synatx:lambda arguments: expression

func=lambda x: x+1

out=func(10)
print(out)


out=func(1000000000)
print(out)



out=lambda x,y: x+y  #lambda is single line function
print(out(10,1))



