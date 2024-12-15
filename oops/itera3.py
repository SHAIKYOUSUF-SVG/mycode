

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
#l.append(100) #'mylist' object has no attribute 'append'
print(l)

class myl:
    def __init__(self,*objs):
        self.li=[]
        for i in objs:
            if type(i)==int:
                self.li.append(i)
            else:
                print('Error')
    def __str__(self):
        return str(self.li)


a=myl(1,2,3,4,5,'usuf')

print(a)