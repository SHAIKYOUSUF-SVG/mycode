l=[0,1]
while len(l)<10:
    l.append(l[-1]+l[-2])
print(l)