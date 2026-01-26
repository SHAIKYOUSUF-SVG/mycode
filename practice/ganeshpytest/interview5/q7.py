#protected class

#how to access private attributes in another class
#actually private attributes cant access from another class
class student:
    def __init__(self,name,rno):
        print("init")
        self._name=name
        self._rno=rno
    def get_name(self):
        return self._name
class marks(student):
    #private attributes cant be access from outside the defined class
    def get_rno(self):
        return self._rno


s1=student("rakesh",1234)
m1=marks("suresh",123)
print(m1.get_rno())







print("ouside",m1._rno)


'''
public attributes:
pub;ic attributes we can from anywhere
protect atrributes featrure and are similar to public
private attrobutes:
we can access only with in class
cannopt be access in dervived class also
can not access from outside also
protected attributes:
should be able to use insoide the class and 
also derived class and not able to access it form out isde the class

'''