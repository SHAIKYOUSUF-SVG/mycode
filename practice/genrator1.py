def gen():
    print("hi")
    yield "A"
    print("hello")
    yield "B"
ge=gen()
# print(next(ge))
# print(next(ge))
for i in ge:
    print(i)

import sys
import time
start=time.time()
def squres():
    for i in range(2,100000000000000000000000):
        yield i*i
out=squres()
end=time.time()
ttime=end-start
print(ttime,"seconds")
print(sys.getsizeof(out),"kb")

start=time.time()
class itera:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        #print("form iter")
        #return True
        return self
    def __next__(self):
        #print("from next")
        if self.start<self.end:
            i=self.start*self.start
            self.start=self.start+1
            return i
        raise StopIteration


out1=itera(2,10)
for i in out1:
    print(i)
end=time.time()
ttime=end-start
print(ttime,"sec")
# print(out1.__iter__())
# print(out1.__next__())
print(sys.getsizeof(out1))