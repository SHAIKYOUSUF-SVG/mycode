#the private methdo can be called inside the class but cant be caled ouside the class

class bank:
    def __init__(self,an,name):
        self.__an=an
        self.__name=name
    def __get_an(self):
        return self.__an

b1=bank(123456,"ramesh")
#print(b1.__get_an())  with this we cant get result
print(b1._bank__get_an())