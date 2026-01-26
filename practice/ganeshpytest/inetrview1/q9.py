#pass by value


def test(data):
    data.append("yousuf")





inp=[1,2,3,4]
test(inp.copy()) #do shallow copy for pass by value if that is one layer
print(inp)


#if has 2layers
#do deep copy

import copy
def test(data):
    data.append("usuf")


inp=[1,2,3,[4,5,6]]
test(copy.deepcopy(inp))
print(inp)




#     0 1 2 ---3---
list=[1,2,3,[4,5,6]]
print(list[0])


fw=open("q10.py","w")
fw.close()