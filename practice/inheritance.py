#inheritance:accessing properties of parent class from child class
class bank:
    def __init__(self,an,name):
        self.an=an
        self.name=name
    def get_an(self):
        return self.an
class savingsbank(bank):
    def get_name(self):
        return self.name
s1=savingsbank(123,"arjun")

print(s1.get_an())
#multi level inheritance:accssing the properties of 2 parent cls from 1 chidl class

class bank:
    def __init__(self,an,name):
        self.an=an
        self.name=name
    def get_an(self):
        print("from parent cls")
        return self.an
    def get_name(self):
        return self.name
class salarybank(bank):
    def __init__(self,an,name,salary):
        bank.__init__(self,an,name)
        #super().__init__(self,an,name)
        self.salary=salary
    def get_an(self):
        print("from child cls")
        super().get_an()
        return self.an

s1=salarybank(123,"ramesh",150000)
out=s1.get_an()
print(out)

#super() key word is used to set the order of calling

print("#####################################")
class cls1:
    variable = "python"

    def __init__(self, an):
        self.an = an
    def get_method1(self):

        return self.an
class cls2(cls1):
    def get_method2(self):
        print(cls2.mro())
        a = cls1.variable
        b = super().get_method1()
        # b=cls1.get_method1()
        # b=C.get_method1()
        return a, b


C = cls2(123)
print(C.get_method2())


############################################################################
#inheritance with out contructor
class cls1:
    def __init__(self,total,female,male):
        self.total=total
        self.female=female
        self.male=male
    def get_total(self):
        return self.total
    def get_male(self):
        print("from main class")
        return self.male
class cls2(cls1):
    def __init__(self,total,male,female):
        super().__init__(total,male,female)
        # self.total=total
        # self.male=male
        # self.female=female
    def get_male(self):
        print("from child class")
        super().get_male()
        return self.male
c2=cls2(200,120,80)

print(c2.__dict__)
print(c2.get_male())



#methods inheritance
class A:
    def __init__(self,b):
        self.b=b

    def meth1(self,b):
        print(b)
class B(A):
    def meth2(self,b):
        A.meth1(self,b)#accessing parent class method with class name
        super().meth1(b)#accessing parent class method woth super()
        return True
obj1=B()
obj1.meth2('b')




















