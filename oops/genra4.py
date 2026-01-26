#writting to get squares in genrator method

def squares(x,y):
    for i in range(x,y+1):
        yield(i*i)


a=squares(2,10)
for i in a:
    print(i)
    #input()

def squares(x,y):
    for i in range(x,y+1):
        yield i*i


out=squares(2,10)
#print(out) will not work in ,and shows as genrator
'''i=next(out)
print(i)
i=next(out)
print(i)
i=next(out)
print(i)
intead of using for every time we loop here'''
for i in out:

    print(i)