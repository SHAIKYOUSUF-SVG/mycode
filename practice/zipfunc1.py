list1=['esuf','usuf','yousuf']
list2=[20,30,40]
for i,j in zip(list1,list2):
    print(f"{i}:{j}")

dict1={'esuf':20,'yousuf':40,'usuf':30}
key,values=zip(*dict1.items())
print(key,type(key))
print(values,type(values))