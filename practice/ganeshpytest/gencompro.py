l=[1,2,3,4,5,6]
out=(i for i in l if i%2==0)
i=next(out)
print(i)
for i in out:
    print(i)