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
'''
this is iteartion ,not looping
if we dont use raise stopiteration then it will not 
it is infinte iteration
to stop we wrote riase stopiteration
'''
sq=squares(2,10)
for i in sq:
    print(i)
    input()