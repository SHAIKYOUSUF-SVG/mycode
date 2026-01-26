class cls1:
    def meth1(self,x,y):
        return x+y
    def meth2(self,*args):
        return sum(args)
out=cls1()
print(out.meth1(10,10))
print(out.meth2(10,100,67))