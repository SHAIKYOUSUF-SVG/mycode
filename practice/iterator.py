#iterator is aan object used to get the values one by one
#__iter__ and __next__ will be in iteration
#
# d1={"a":100,"b":200,"c":300}
# d2={"a":100,"b":100,"d":500}
# d3={}
#
# for i,j in d2.items():
#     if i in d1.keys():
#         d3[i]=d1[i]+d2[i]
#     else:
#         d3[i]=d2[i]
# print(d3)
#__iter__ will be called only once
class squares:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        print("i ma in iter")
        return self
        #return self
    def __next__(self):
        if self.start <self.end:
            out=self.start*self.start
            self.start=self.start+1
            return out
        raise StopIteration
sq=squares(2,10)
for i in sq:
    i=str(i)
    i.strip()
    print(i)



