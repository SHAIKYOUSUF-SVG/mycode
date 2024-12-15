class mylist:
    def __init__(self,*objs):
        self.data=[]
        for i in objs:
            if i not in self.data and type(i) == int:
                self.data.append(i)
    def __str__(self):
        return str(self.data)
    def append(self,obj):
        if type(obj)==int:
            self.data.append(i)
    def insert(self,index,obj):
        self.data.insert(index,obj)
    def pop(self,index):
        self.data.pop(index)
    def remove (self,obj):
        self.data.remove(obj)
    def clear(self):
        self.data.clear()
    #def extend(self,*objs):

    #    self.data.extend(str(*objs))


x=mylist(10,20,20,"ji","iui",10)
print(x)

x.insert(0,1234)
x.pop(1)
x.remove(1234)
x.clear()
print(x)
#x.extend(1,2,3)
#print(x)