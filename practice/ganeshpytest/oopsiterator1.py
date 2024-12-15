
import sys
import time
start=time.time()
class cubes:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start<=self.end:
            out=self.start*self.start
            self.start+=1
            return out
        raise StopIteration
cb=cubes(1,1000000000000000000000000000000000)
end=time.time()
ttime=end-start
print(ttime,'seconds')
size=sys.getsizeof(cb)
print(size,'bytes')


#genrator
start=time.time()
def cubes(x,y):
    for i in range(x,y+1):
        yield i*i*i

c=cubes(1,1000000000000000000000000000000000)
end=time.time()
ttime=end-start
print(ttime,'seconds')
size=sys.getsizeof(c)
print(size,'bytes')


