class myls:
    def __init__(self,*opts):
        self.data=[]
        for i in opts:
            if type(i)==int:
                self.data.append(i)
    def __str__(self):
        return str(self.data)
    def append(self,arg):
        self.data.append(arg)
    def insert(self,index,obj):
        self.data.insert(index,obj)
    def pop(self):
        self.data.pop()
    def remove(self,obj):
        self.data.remove(obj)
    def copy(self):
        self.data.copy()
    def clear(self):
        self.data.clear()
    def extend(self,l):
        self.data.extend(l)


ls=myls(1,2,3,4,5,6,'ddnd')
#print(ls.data)
ls.append(100)
ls.insert(0,989)
ls.pop()
ls.remove(4)
ls.copy()
#ls.clear()
ls.extend([33,44,22])
print(ls)