class A:
    x=10
    y=20
    def __init__(self,a):
        self.a=a
    def meth1(self,arg1):
        self.arg1 = arg1
        return self.arg1 +self.a
    @classmethod
    def class_method(cls):
        pass
    @staticmethod
    def static_method():
        pass

#instance method
class A:
    def instance_method(self,arg1):
        return arg1
obj=A()
print(obj.instance_method('hio'))


#class method

class A:
    var1=10
    var2='python'
    @classmethod
    def class_method(cls):
        return cls.var1
obj=A()
print(obj.class_method())


#static method


class A:
    @staticmethod
    def static_method():
        return "hi"

obj=A()
print(obj.static_method())

'''
class A:
    __init__
    reboot method
class B(A):
    if server_status==on:
        msg
    else:
     class reboot method
'''