list1=[10,20,30]
list2=list1.copy()
'''
to check the memory address
when run this code,the output will show 2 different  memory addresses because list1 and list2 are 2 distinct 
lists,even though they have same content'''

print(list1,id(list1))
print(list1[0],id(list1[0]))

print(list2,id(list2))
print(list2[0],id(list2[0]))





list=[[10,20],[30,40],[540,60]]  #this multi layer/multi ndimentional
list1=list.copy()

print(list,id(list))
print(list[0],id(list[0]))
print(list1,id(list1))
print(list1[0],id(list1[0]))
import copy
l1=[[10,20],[30,40],[540,60]]
l2=copy.deepcopy(l1)

l3=copy.copy(l1)

print("l1 id is",id(l1),id(l1[0]),id(l1[0][0]))
print("l2 id is",id(l2),id(l2[0]),id(l2[0][0]))
print("l3 id is",id(l3),id(l3[0]),id(l3[0][0]))
