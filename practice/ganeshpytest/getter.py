'''
getter ,ethod:
cslling [rivste attributes/methods outside the class
'''

class A:
    def __init__(self,arg1):
        self.__arg1=arg1
    def __private_method(self):
        return 'oprivate mrthod'
    def getter_method(self):
        return self.__arg1
obj1=A(110)
print(obj1._A__private_method())
print(obj1.getter_method())


'''name Mangling:
combining class name with object name
to access the private attributes outside the class'''
