import sys
class squares:
    def __init__(self,start,end):
        self.start=start
        self.emd=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start<=self.end:
            x=self.start*self.start
            self.start+=1
            return x
        raise StopIteration
out=squares(2,100000000000000000000000000000)
out1=sys.getsizeof(out)
print(out1)