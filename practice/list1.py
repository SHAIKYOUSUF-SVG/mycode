l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[]
for i in l1:
    l2.append(i[0])
    l2.append(i[1])
    l2.append(i[2])
print(l2)

l3=[]
for i in l1:
    if type(i)==str:
        l3.append(i)
    if type(i)==list:
        l3.extend(i)
print(l3)






