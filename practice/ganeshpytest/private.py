'''
private Attributes/Methods
 we cant access private attributes/ methods directly outside the class
 we defien the prtivate attributes/ emthod with prifix '__'
'''

class A:
    def __init__(self):
        self.__arg1="prptected"
    def __private_method(self):
        return "private method"

obj=A()
print(obj._A__arg1)
print(obj._A__private_method())

