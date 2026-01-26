
def func(x):
    def wrapper(*args):
        for a in args:
            if type(a)!=int:
                return "invalid input"
        out=x(*args)
        return out

    return wrapper

@func
def add(x,y):
    return x+y

a=add(10,10)
#a=add('a','aa')
print(a)