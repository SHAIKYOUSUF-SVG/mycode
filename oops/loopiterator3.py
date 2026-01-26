#we cants use loop on iteartion
#with __iter__  cqll __iter__ and show some error to avoid that error erite __next__
#for that we need __iter__ and __next__


class squares:
    def __init__(self,a,z):
        self.a=a
        self.z=z
    def __iter__(self):
        print("am in iter")
        return self
    def __next__(self):  #__next__ is infinite loop it will not stop
        print("am in next")
        return "yousuf"

sq=squares(2,10)
for i in sq:
    print(i)
    input()

