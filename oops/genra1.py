'''
generator is a function with yield instead of return
when we use genratir,genrsto function will start to excute the code amd pause at
yield statement
'''

def test():
    print("a")
    return 10

a=test()
print(a)

def test1():
    print("a")
    yield 10
z=test1()
print(z)

