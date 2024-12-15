#__iter__is iter only once but __next__ is infinite loop it will not stop until we stop
# i want to caluclate the squares and written the value hav ehot after return yousuf
class squares:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= self.end: #for stop at a point we use/give end point
            out=self.start*self.start
            self.start =self.start+1
            return out
sq=squares(2,10)
for i in sq:
    print(i)