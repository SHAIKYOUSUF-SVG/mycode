'''
does python supports  function overloading-no
'''


def add(x,y):
    return x+y

def add(x,y,z):
    return x+y+z

out=add(10,10,10)
print(out)
'''
if 2 function are with same names.then latest func will execute old will not execute
means it will over write
not overload'''


def add(*obj):
    if len(obj)==2:
        return obj[0]+obj[1]
    if len(obj)==3:
        return obj[0]+obj[1]+obj[2]

out=add(1,2,)
print(out)



def mul(*obj):
    if len(obj)==2:
        return obj[0]*obj[1]
    if len(obj)==3:
        return obj[0]*obj[1]*obj[2]
out1=mul(23,10,35)
print(out1)

def add1(*args):
    if len(args)==2:
        return args[0]+args[1]
    if len(args)==3:
        return args[0]+args[1]+args[2]
out=add1(2,2,100)
print(out)


