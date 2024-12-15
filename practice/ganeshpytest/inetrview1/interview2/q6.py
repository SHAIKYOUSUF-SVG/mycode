#to get out of funtion overloading
#we write args in optional arguimnets

#optinal arguments result in tuple
def add(*objs):
    if len(objs)==2:
        return objs[0]+objs[1]
    if len(objs)==3:
        return objs[0]+objs[1]+objs[2]



out=add(10,5)
print(out)

out=add(10,10,10)
print(out)