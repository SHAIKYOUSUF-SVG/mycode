class mylist:
    def __init__(self,*objs):
        self.data=[]
        for i in objs:
            if type(i) == int:
                self.data.append(i)
    def __str__(self):
        #return self.data
        return str(self.data)


l=mylist(1,2,3,4,"hi","hello")
l.data.append(100)
print(l.data)

print(l.data)

print("l is",l,type(l))