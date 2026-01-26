class squares:
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
sq=squares(1,100000000000000000)
for i in sq:
    print(i)
    input()
