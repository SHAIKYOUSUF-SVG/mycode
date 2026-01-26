#defining multiple functions with same names and different no.of arguments or different no of arguments

def add(x,y):
    return x+y
def add(x,y,z):
    return x+y+z
#when we wrote 2 functions with same names then latest function will take old one will not come
#print(add(1,2))  #this will not run shows like 1missing positional argument
print(add(1,2,3))

#to overcome this we take optinal arguments
def add (a,b,c=0):
    return a+b+c
print(add(1,2))
print(add(10,20,30))


#overloading
def add(x,y):
    if type(x)==int and type(y)==int:
        return x+y
    if type(x)==list and type(y)==list:
        return len(x)+len(y)
out=add(12,23)
print(out)
x=[1,2,3,4]
y=[9,8,7,6]
print(add(x,y))


def mul(x,y):
    return x*y
def mul(x,y,z=1):
    return x*y*z

print(mul(10,10))


def add1(x,y):
    return x+y
def add1(x,y,z=0):
    return x+y+z
out=add1(1,2)
print(out)

def mul1(x,y):
    return x*y
def mul1(x,y,z):
    return x*y*z
out2=mul1(10,10,10)
print(out2)

def sq1(x,y):
    return y**x
def sq1(x,y,z=0):
    return x**y**z
out=sq1(2,3)
print(out)

