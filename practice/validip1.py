import re

data='192.168.0.113'
exp='(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})'
out=re.search(exp,data)
if out:
    if int(out.group(1))<256 and int(out.group(2))<256 and int(out.group(3))<256 and int(out.group(4))<256:
        print('valid ip')
    else:
        print('invalid ip')

def update(data,new=[]):
    print(globals())
    print(locals())
    new.append(data)
    return new
res=update('hi')
res=update('hello')
res=update('welcome')
print(res)

def func(x,lst=[]):
    lst.append(x)
    return lst
print(func(1))
print(func(2))
print(func(3))


def outer():
    x=10
    def inner():
        return x
    return inner()
f=outer()
print(f)


def add(x,y):
    return x+y
out=add(*[1,2])
print(out)

def func(a=[]):
    a.append(1)
    return a
print(func())
print(func())
print(func())


def fun(a):
    out=set(str)
    


str = 'aabbaa'
fun(str)
# print(str.count('a'))