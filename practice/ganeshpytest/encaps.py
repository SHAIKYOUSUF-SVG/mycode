'''
Encapsulation:
bundling the data and methods into a class
it's a way to proctect classes from accidental changes or deletions,
'''

class Enc:
    def __init__(self,a,b,c):
        self.a=a
        self._b=b
        self.__c=c
    def __private_method(self):
        return self.a
    def setter_method(self,new):
        self.__c=new
    def getter_method(self):
        return self.__c

obj=Enc('a','b','c')

obj.setter_method("usuf")
print(obj.getter_method())