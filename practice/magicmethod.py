'''
__str__
__add__
__init__
__del__ destructor
these all are magic methods:they are called automatically when we initialize the cls
'''
#using  __add__ methdo

class test:
    def __init__(self,*args):
        self.data=[]
        for i in args:
            if type(i)==int:
                self.data.append(i)
    # def __add__(self,arg1):
    #     all_data=self.data+arg1.data
    #     print(all_data)
    #     out=sum(all_data)
    #     return out
    def __add__(self,arg1):
        alldata=self.data+arg1.data
        out=sum(alldata)
        return out


t1=test(10,20,30,"india",9)
t2=test(12,3,4,5,6)

out=t1+t2
print(out)

print("#########################")
class test:
    def __init__(self,*args):
        self.data=[]
        for i in args:
            if type(i)==int:
                self.data.append(i)
    #__add__ will call auto justlike __init__
    def __add__(self,arg):
        all_data=self.data+arg.data

        out=sum(all_data)
        out=test(out)
        return out




t1=test(1,2,3,4,5,6,7,8)
t2=test(2,345,4,)
t3=test(37,383)
out=t1+t2+t3
print(out,out.data)


