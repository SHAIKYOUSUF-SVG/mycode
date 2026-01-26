import time
import sys

start=time.time()
class squares:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= self.end:
            out=self.start*self.start
            self.start=self.start+1
            return out  #ater 10 we get none w=values will not stop iteration
        #need to stop iteration
        raise StopIteration #we cant use brank this is not loops
sq=squares(2,10000000000000000)
end=time.time()
out=start-end
print(out)

out1=sys.getsizeof(out)
print("size is",out1)

#size and time are smaller than genrator

"""
def __iter__(self):
    return self
def __next__(self):
    if self.a<=self.z:
        out=self.a*self.a
        self.a+=1
        return out
    raise StopIteration 
"""
