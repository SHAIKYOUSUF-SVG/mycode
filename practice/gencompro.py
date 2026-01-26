l2=["india","uk","us","germany","france"]
out=(i for i in l2)
for i in out:
    print(i)


l1=[1,2,3,4,5]
out=(i+i for i in l1)
a=next(out)
print(a)

for i in out:
    print(i)


str="bcby bcdbuwb efby"
out1=str.split(" ")
print(out1)
gc=(i for i in out1 if len(i)>=4)
print(list(gc)) #or for i gc print(i)
dc={i:len(i) for i in out1}
print(dc)


str1="yousuf esuf usuf"
out=str1.split(' ')
print(out)
gc1=(i for i in out if len(i)>=4)
# print(list(gc))
for i in gc1:
    print(i)

s1='yousuf esuf usuf'
out=s1.split()
lc=[i for i in out]
print(lc)

