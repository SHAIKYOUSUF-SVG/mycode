n=5
k=True
for i in range(2,n):
    if n%i==0:
        k=False
        break
if k==True:
    print('it is prime')
else:
    print('not a prime num')

n=10
for i in range(2,n):
    if n%i==0:
        k=False
        break
if k==True:
    print('it is prime')
else:
    print('not a prime')

l=[]
for i in range(1,100):
    k=True

    for num in range(2,i):
        if i%num==0:
            k=False
            break
    if k:
        l.append(i)
print(l)




