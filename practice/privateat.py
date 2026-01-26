#how to call private attributes from another class

class student:
    def __init__(self,name,phnum,cls):
        self.__name=name
        self.__phnum=phnum
        self.__cls=cls
    def get_name(self):
        return self.__name
    def __get_cls(self):
        return self.__cls

class bio(student):
    def get_name(self):
        return self._student__name

b1=bio("rahul",9874648323,10)
print(b1.get_name())

print(b1._student__get_cls())