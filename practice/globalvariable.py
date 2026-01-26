#in python any data  it acts as a global except in function
#in functions it will acts as local
#to make it global we can do 2 tings
#we can use return statement or we can write globale name



def func():
    print("hi,this is yousuf")
    x=10
    print(x)
func()
def func():
    print("hi,this is yousuf")
    x=10
    print(x)
    return x
out=func()
print(out)

#here x is local we cant get this from outside to get ouside


def func():
    global x
    print("hi,this is yousuf")
    x=10
    print(x)
func()
print(x)   #this is how we make a variable global inside a function



def func1():
    x=10
    y=20
    print('x is ',x)
    print('y is ',y)
    print('z is ',z)
y=100
z=200
func1()
print('from outisde y is ',y)
print('from outside z is ',z)