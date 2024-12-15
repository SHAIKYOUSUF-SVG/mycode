


class test:
    def __init__(self,*args):
        self.data=[]
        for i in args:
            if type(i)==int:
                self.data.append(i)

    def __add__(self,arg1):
        alldata=self.data+arg1.data
        out=sum(alldata)
        out=test(out)
        return out
t2=test(2,3,4,5,6,7)
t1=test(1,2,3)
result=t2+t1
print(result,result.data)