def squares(x,y):
    tmp=[]
    for i in range(x,y+1):
        tmp.append(i*i)
    return tmp
out=squares(2,100)
print(out)