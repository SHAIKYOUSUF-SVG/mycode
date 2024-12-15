import time
import sys
start=time.time()
class cubes:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        print("i ma in iter")
        return self
    def __next__(self):
        if self.start<=self.end:
            x=self.start*self.start*self.start
            self.start += 1
            return x
        raise StopIteration
obj=cubes(2,100000000000)

end=time.time()
out1=end-start
print(out1)
print(sys.getsizeof(obj))