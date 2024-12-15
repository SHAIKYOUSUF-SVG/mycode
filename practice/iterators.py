

#normal iterator
import time
import sys
start=time.time()
def sqaures(x,y):
    l=[]
    for i in range(x,y+1):
        l.append(i*i)
    return l
out=sqaures(2,90000000)
# out=sqaures(2,100000000000000000000000000000000000)
end=time.time()
tt=end-start
print(tt,"sec")
size=sys.getsizeof(out)
print(size,"bytes")


#oops iterator
start=time.time()
class squares:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        print("from iter")
        return self
    def __next__(self):
        if self.start<=self.end:
            out=self.start*self.start
            self.start+=1
            return out
        raise StopIteration
out=squares(2,90000000)
end=time.time()
tt=end-start
print(tt,'sec')
size=sys.getsizeof(out,)
print(size,"bytes")

#genratir function used to genrate the sequesnce of variblaes falsty and in lesstime and in less size
# in genrator insted of return we use yield statement


import time
import sys

start=time.time()
def sqaures(x,y):
    for i in range(x,y+1):
        #return i*i
        yield i*i
out=sqaures(2,90000000)
end=time.time()
tt=end-start
print(tt,"sec")
size=sys.getsizeof(out)
print(size,"bytes")


