'''
creating our own list
'''

class mylist:
    def __init__(self,*obj):
        self.data=[]
        for i in obj:
            if type(i) == int:
                self.data.append(i)


l1=mylist(10,20,30,"hi","hello")
print(l1.data)




x1=mylist(1,2,3,4,5,6,7,8,9,0,"d","s","e","e","d",)
print(x1.data)