'''
how to know how much time takes to run prograne time.time()
how to know the size of object is :sys.getsizeof()
'''

import sys
import time

start=time.time()
def squres(x,y):
    t=[]
    for i in range(x,y+1):
        t.append(i*i)
    return t
a=squres(2,100)
print(a)
end=time.time()
out=start-end
print(out)


size=sys.getsizeof(out)
print(size,"bytes")