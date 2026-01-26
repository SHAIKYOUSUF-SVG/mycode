a=10
b=a
print(id(a))
print(id(b))

#genrerlly python will take value ''by referrence''
#in pass by refference id of every iteration will be not same
#id will be uniq is pass by refference


#example for pass by reference
list=[[10,20],[30,40],[540,60]]
list1=list

print(list[0],id(list[0]))
print(list1[1],id(list1[1]))
print("example for shallow copy")
list2=[[10,20],[30,40],[540,60]]
list3=list2.copy()

print(id(list2))
print(id(list3))


print(list2[0],id(list2[0]))
print(list3[0],id(list3[0]))

print(list2[0][0],id(list2[0][0]))
print(list3[0][0],id(list3[0][0]))

import copy
print("ex for deepcopy")
list4=[[1,20],[30,40],[540,60]]
list5=copy.deepcopy(list4)



print(id(list4))
print(id(list5))


print(list4[0],id(list4[0]))
print(list5[0],id(list5[0]))

print(list4[0][0],id(list4[0][0]))
print(list5[0][0],id(list5[0][0]))



import re
line = "Cats are smarter than dogs";
searchObj = re.search( r"(.*) are (.*?) .*", line, re.M|re.I)
if searchObj:
    print ("searchObj.group() : ", searchObj.group())
    print ("searchObj.group(1) : ", searchObj.group(1))
    print ("searchObj.group(2) : ", searchObj.group(2))
else:
    print ("Nothing found!!")
# r'(.*) are (.*?) .*'



def atest(data):
    data.append("yousuf")





inp=[1,2,3,4]
atest(inp.copy()) #do shallow copy for pass by value if that is one layer
print(inp)


import copy
def aatest(data):
    data.append("usuf")


inp=[1,2,3,[4,5,6]]
aatest(copy.deepcopy(inp))
print(inp)



