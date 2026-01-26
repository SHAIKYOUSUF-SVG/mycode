#to make any class iterable
#use __iter__
'''
__iter__method will be called only in first iteration
'''
class squares:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self): #when start looping, __iter__ will class but only once
        print("am in iter....")
        return self
sq=squares(2,10)
for i in sq:
    print(i)