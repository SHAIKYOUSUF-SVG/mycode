# list=[]
# for i in range(0,11):
#     list.append(i+(i+1))
# print(list)


def feb(n):
    feb_list=[0,1]
    while len(feb_list)<n:
        feb_list.append(feb_list[-1]+feb_list[-2])
    return feb_list
n=10
print(feb(n))


def feb(n):
    feb_list=[0,1]
    while len(feb_list)<n:
        feb_list.append(feb_list[-1]+feb_list[-2])
    return feb_list
n=20
print(feb(n))


#wrong
# def fib(n):
#     first=0
#     second=1
#     l=[first,second]
#     for i in range(n):
#         third=first+second
#         fourth=second+third
#         l.extend([third,fourth])
#         first=third
#         second=fourth
#     return l
# out=fib(10)
# print(out)


func=lambda x,y:x+y
out=func(10,10)
print(out)


l=[1,2,3,4,5]
out=l[::-1]
print(out)

l=[3,6,32,12,52,123]
l.sort()
print(l)
out=sorted(l,reverse=True)
print(out)


#anagram
a='silent'
b='listen'
c=True
if len(a)!=len(b):
    c=False
if c:
    if sorted(a)==sorted(b):
        print('anagram')
    else:
        print('not an anagram')



#decorator
def func(n):
    def wrapper(*args):
        #global total
        out=n(*args)
        return out
    return wrapper
def func(s):
    def wrapper(*args,**kwargs):
        out=s(*args,**kwargs)
        return out
    return wrapper
@func
def add(x,y):
    return x+y
print(add(1,1))

#febno
def feb(n):
    feb_list=[0,1]
    while len(feb_list)<n:
        feb_list.append(feb_list[-1]+feb_list[-2])
    return feb_list
out=feb(10)
print(out)

l=[0,1]
while(len(l))<10:
    l.append(l[-1]+l[-2])
print(l)


import paramiko

client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='',username='',passwprd='')
a,b,c=client.exec_command('code')
out=b.read().decode().strip()
print(out)
out.close()
