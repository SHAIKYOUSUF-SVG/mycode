#protected:


class A:
    def __init__(self):
        self._arg1="protected Attribute"
obj1=A()
print(obj1._arg1)


class A:
    def __init__(self,arg1):
        self._arg1=arg1
    def _meth1(self):
        return "this is protected method"
    def _meth2(self):
        return self._arg1
obj2=A('100')
print(obj2._arg1)
print(obj2._meth1())
print(obj2._meth2())