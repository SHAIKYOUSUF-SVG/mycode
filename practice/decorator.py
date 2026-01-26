#decorator:a function use3ed to modify another funtion with modify original funtion

def checking(func):
    def wrapper(*args,**kwargs):
        '''
        func(*args,**kwargs)
               '''
    return wrapper()
@checking
def div(a,b):
    return a/b

'''
A decorator in Python is a design pattern that allows you to modify the 
behavior of a function or method without changing its actual code. 
Decorators are typically used to extend the functionality of a function 
in a clean and readable manner. They are often applied in scenarios 
like logging, authentication, or timing function execution.

How Decorators Work:
A decorator is a higher-order function that takes a function as an 
argument, adds some behavior to it, and returns a new function. 
This is done using the @decorator_name syntax, placed just before 
the function you want to decorate'''

def my_decorator(func):
    def wrapper():
        print("Something before the function.")

        print("Something after the function.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


'''
output:
Something before the function.
Hello!
Something after the function.
'''

'''explanation:
'''
import time
def func(x):
    def wrapper(*args):
        global total
        start=time.time()
        out=x(*args)
        end=time.time()
        total=end-start
        return out
    return wrapper

@func
def add(x,y):
    time.sleep(5)
    return x+y

@func
def mul(x,y,z=0):
    return x*y*z

print(add(101,10))

print(mul(1,2))
print(total)


def feb(n):
    feb_list=[0,1]
    while len(feb_list)<n:
        feb_list.append(feb_list[-1]+feb_list[-2])
    return feb_list
n=10
print(feb(n))


class shoppingcart:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    