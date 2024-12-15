#how to access private attributes in another class
#actually private attributes cant access from another class
class student:
    def __init__(self,name,rno):
        print("init")
        self.__name=name
        self.__rno=rno
    def get_name(self):
        return self.__name
class marks(student):
    #private attributes cant be access from outside the defined class
    def get_rno(self):
        return self.__rno


s1=student("rakesh",1234)
m1=marks("suresh",123)
print(m1.get_rno())


'''
public attributes:
pub;ic attributes we can from anywhere
private attrobutes:
we can access only with in class
protected attributes:
should be able to use insoide the class and also derived class and not able to access it form out isde the class

'''