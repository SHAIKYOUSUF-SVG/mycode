#__iter__is iterate only once but __next__ is infinite loop it will not stop until we stop
# if want to calculate the squares and written the value have hot after return yousuf
class squares:
    def __init__(self,a,z):
        self.a=a
        self.z=z
    def __iter__(self):
        return self
    def __next__(self):
        #print("am in next",self.a)
        #if self.a<=self.z:
        out=self.a*self.a
        self.a += 1
        return out
sq=squares(2,10)
for i in sq:
    print(i)
    input()

class cube:
    def __init__(self,s,d):
        self.s=s
        self.d=d
    def __iter__(self):
        return self
    def __next__(self):
        print('from next')
        out=self.a*self.a
        return out
        # self.a+=1
        # if self.a>self.d:
cu=cube(2,10)
for i in cu:
    print(i)