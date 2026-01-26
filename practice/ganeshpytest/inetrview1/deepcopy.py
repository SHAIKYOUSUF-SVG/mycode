# print("ex for deepcopy")
list4=[[10,20],[30,40],[540,60]]
list5=copy.deepcopy(list4)



print(id(list4))
print(id(list5))


print(list4[0],id(list4[0]))
print(list5[0],id(list5[0]))

print(list4[0][0],id(list4[0][0]))
print(list5[0][0],id(list5[0][0]))