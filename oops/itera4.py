class mylist:
    def __init__(self,*objs):
        self.data=[]
        for i in objs:
            if type(i) == int:
                self.data.append(i)
    def __str__(self):
        #return self.data
        return str(self.data)
    def apppend(self,obj):
        if type(obj)==int:
            self.data.append(obj)


l=mylist(1,2,3,4,"hi","hello")
l.apppend(1000)
print(l)