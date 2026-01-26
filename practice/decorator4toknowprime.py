def func(x):
    def wrapper(arg):
        k=True
        for num in range(2,arg):
            if arg%num==0:
                k=False
                break
        if k:
            return f'{arg} is a prime'
        else:
            return f'{arg} not a prime'
    return wrapper

@func
def prime(arg):
    return arg
print(prime(10))
print(prime(7))


def checkprime(x):
    def wrapper():
        l=[]
        for num in range(2,100):
            k = True
            for i in range(2,num):
                if num%i==0:
                    k=False
                    break
            if k:
                l.append(num)
        return l
    return wrapper

@checkprime
def prime_list():
    return l
print(prime_list())