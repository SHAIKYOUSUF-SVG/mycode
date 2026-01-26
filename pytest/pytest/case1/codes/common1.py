def common(l1,l2):
    l3=[]
    for i in l1:
        if i in l2:
            l3.append(i)
    return l3

#uniq
def uniq(obj):  #[10,2,1,4,10,10]
    u=[]
    #for i not in u:
    for i in obj:
        if i in u:
            u.append(i)
    return u
'''
def uniq(obj):
    u=[]
    for i in obj:
        if i not in u:
            u.append(i)
    return u
y=[1,2,3,4,1,2]
out=uniq(y)
print(out)'''

