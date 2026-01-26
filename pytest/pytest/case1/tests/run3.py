def uniq(obj):
    u=[]
    for i in obj:
        if i not in u:
            u.append(i)
    return u
y=[1,2,3,4,1,2]
out=uniq(y)
print(out)