#how to create our own iterator
#to make any class iterable,define a special methods __iter__,__next__

class squares:
    def __init__(self,a,b):
        self.a=a
        self.b=b
sq=squares(2,10)
for i in sq:
    print(i)

#'squares' object is not iterable
'''
we cant use loop for our own classes
our own methods/class are not iterable

soooo
wrote __iter__ for iterable
'''

class cubes:
    def __init__(self,aa,bb):
        self.aa=aa
        self.bb=bb
    def __iter__(self):
        print("for iter")
        return self

cub=cubes(2,10)
for i in cub:
    print(i)

