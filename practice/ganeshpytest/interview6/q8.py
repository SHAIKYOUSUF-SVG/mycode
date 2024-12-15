#what is magic methods?  also know as dunder methdod
#__init__,__str__ ,__all__are also comes under magic methdo we calls automatically


#what is opeartor overloading?

class test:
    def __init__(self,*args):
        self.data=[]
        for i in args:
            if type(i) ==int:
                self.data.append(i)


t1=test(10,20,30,"india",40)
t2=test(11,2,3,4,5)
#print(t1.data)
#print(t2.data)

#print(t3) it will not do concatination for that we write a maguc method __all__ to operatpr overloading
